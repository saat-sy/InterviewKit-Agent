from langchain_core.prompts import ChatPromptTemplate
from agent.models.plan import Plan
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
"""
    )
    return prompt | get_llm().with_structured_output(Plan)

def get_replanner_template():
    prompt = ChatPromptTemplate.from_template(
        """
You are the Interview Replanning Agent. Based on the feedback summary and interview progress:

1. Identify areas that require deeper exploration
2. Determine if initial assumptions about candidate strengths/weaknesses were accurate
3. Adjust the remaining interview focus to address gaps in evaluation
4. Prioritize follow-up questions for the next interview segment
5. Decide if specialized technical assessments are needed

These are the original steps planned:
{plan}

These are the steps already executed:
{executed_steps}

Feedback until this point: {feedback}

Create an updated interview plan that addresses any missing coverage of job requirements. If the interview is near completion, determine if sufficient information has been gathered for a comprehensive evaluation.

Your output can either be a Plan if there are more steps left or a boolean indicating if the interview should be finished.
If you want the interview to be over, set it to True.
If there are more steps that you want to execute, use Plan.
"""
    )
    return prompt | get_llm()

def get_feedback_summarizer_template():
    prompt = ChatPromptTemplate.from_template(
        """
You are the Feedback Summarization Agent. Compile and synthesize all feedback collected during the technical interview into a comprehensive summary that:
1. Highlights key strengths demonstrated by the candidate
2. Identifies knowledge or experience gaps relevant to the position
3. Evaluates technical proficiency across required skills
4. Assesses problem-solving abilities and approach
5. Summarizes communication skills and ability to explain complex concepts.

Organize feedback by skill categories aligned with job requirements. Provide specific examples from the interview that support your assessments. Your summary will be used to inform the replanning process and final evaluation report.
"""
    )
    pass

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