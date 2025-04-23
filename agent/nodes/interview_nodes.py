from agent.states.interview_state import InterviewState
from agent.workflows.interview_step_workflow import interview_step_workflow

async def process_resume(state: InterviewState):
    return {
        "raw_resume": "",
        "raw_job_description": "",
        "processed_resume": ""
    }

async def planner(state: InterviewState):
    return {
        "plan": None
    }

async def replanner(state: InterviewState):
    return {
        "plan": None
    }

async def feedback_summarizer(state: InterviewState):
    return {
        "feedback": state["feedback"] + ""
    }

async def final_report_generator(state: InterviewState):
    return {
        "final_report": ""
    }

async def call_technical_interview(state: InterviewState):
    response = await interview_step_workflow().invoke()
    return {
        "feedback": ""
    }

def finish_interview(state: InterviewState):
    return "final_report_generator"