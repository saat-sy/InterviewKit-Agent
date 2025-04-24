from langchain_core.prompts import ChatPromptTemplate
from agent.models.plan import Plan
from agent.models.replan import Replan
from agent.utils.llm_provider import get_llm


def get_process_resume_template():
    prompt = ChatPromptTemplate.from_template(
        """
You are the Resume Processing Agent responsible for analyzing candidate resumes for software engineering positions. Extract key information including:
1. Technical skills and proficiency levels
2. Projects completed with technologies used
3. Role responsibilities and achievements
4. Education and certifications
5. Career progression and timeline

Format this information into structured data that categorizes experiences by relevance to the job description. Identify potential strengths, weaknesses, and areas to probe deeper during the interview. Your output will be used by the Planner agent to structure the technical interview.

Candidate Resume:
{raw_resume}

Job Description:
{raw_job_description}
"""
    )
    return prompt | get_llm()


def get_planner_template():
    prompt = ChatPromptTemplate.from_template(
        """
You are the Interview Planning Agent. Using the structured resume analysis and job requirements, create a comprehensive interview plan that:
1. Prioritizes topics based on relevance to the position
2. Allocates appropriate time to each topic
3. Identifies specific projects from the resume to explore in depth
4. Maps candidate skills against job requirements
5. Determines the sequence of technical questions to ask

Your plan should include specific areas to probe based on potential gaps or strengths identified in the resume. Create a structured interview path that ensures thorough coverage of required skills while maintaining a conversational flow. Your output will guide the technical interview process.

Processed Resume:
{processed_resume}

The total duration of the interview has to be {duration} minutes. So make sure the total time of the plan is equal to that.
"""
    )
    return prompt | get_llm().with_structured_output(Plan)


def get_replanner_template():
    prompt = ChatPromptTemplate.from_template(
        """
# INTERVIEW REPLANNING AGENT

You are the Interview Replanning Agent. Your job is to evaluate the current progress of the interview and intelligently adjust the remaining plan to ensure complete, balanced, and meaningful assessment of the candidate.

## YOUR TASKS
Analyze the following:
1. Which topics or skills are underexplored or missing entirely
2. Whether the initial assumptions about the candidate\'s strengths and weaknesses still hold
3. What follow-up areas or deeper questions are necessary
4. If any specialized assessments (e.g. system design, debugging) are now essential
5. How much interview time remains, and how it should be best used

---

## INPUT CONTEXT

- **Original Interview Plan**:  
{plan}

- **Steps Already Executed**:  
{executed_steps}

- **Feedback Summary So Far**:  
{overall_feedback}

- **Total duration of the interview**:
{duration}

- **Time elapsed**:
{elapsed_time}

---

## OUTPUT FORMAT

You must return **one of two responses**:

### ✅ OPTION 1: Continue Interview
Clearly list:
- The **revised plan** with updated step names, their purpose, and estimated durations.
- Which previous gaps this new plan is addressing.
- Why this adjusted plan is necessary based on the candidate's responses and feedback.

*Example Output:*
> Continue Interview.  
> Remaining steps:  
> 1. System Design Deep Dive (10 mins) – explore architectural reasoning and scalability decisions, not yet evaluated.  
> 2. Debugging Scenario (5 mins) – candidate has mentioned debugging experience but hasn’t been probed in depth.  
> These steps fill gaps in technical evaluation missed earlier.

---

### 🛑 OPTION 2: End Interview  
If no significant value would come from continuing, say:
> End Interview. All critical areas have been adequately explored.  
> Feedback indicates we have enough information for a comprehensive evaluation.

---

## MANDATORY CHECKLIST BEFORE RESPONDING
- Have all core competencies (technical depth, decision-making, communication, and relevant experience) been covered?
- Would more questions **materially improve** the assessment?
- Are you confident enough in the gathered data to **make a hiring decision**?

Be decisive and focused. Only continue the interview if it will **add real insight**.
"""
    )
    return prompt | get_llm().with_structured_output(Replan)


def get_final_report_generator_template():
    prompt = ChatPromptTemplate.from_template(
        """
You are the Final Report Generation Agent. Create a comprehensive evaluation report based on the complete interview data that:

1. Provides an executive summary of the candidate's suitability for the position
2. Evaluates technical qualifications against each job requirement
3. Highlights demonstrated strengths with specific examples from the interview
4. Identifies potential growth areas or skill gaps
5. Recommends next steps (additional interviews, technical assessments, etc.)

Include a quantitative assessment using a standardized rubric covering technical skills, problem-solving, communication, and role-specific requirements. Your report should be balanced, evidence-based, and actionable for hiring decision-makers.
"""
    )
    return prompt | get_llm()
