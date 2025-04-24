from agent.models.replan import Replan
from agent.states.interview_state import InterviewState
from agent.prompts.interview_prompts import (
    get_process_resume_template,
    get_planner_template,
    get_replanner_template,
    get_final_report_generator_template,
)
import time


async def process_resume(state: InterviewState):
    processed_resume = await get_process_resume_template().ainvoke(state)
    return {"processed_resume": processed_resume}


async def planner(state: InterviewState):
    plan = await get_planner_template().ainvoke(state)
    return {"plan": plan}


async def replanner(state: InterviewState):
    next_step: Replan = await get_replanner_template().ainvoke(
        {
            **state,
            "elapsed_time": time.strftime(
                "%H:%M:%S", time.gmtime(time.time() - state["interview_start_time"])
            ),
        }
    )
    if next_step.step_completed:
        return {"interview_completed": True}
    else:
        return {"plan": next_step.plan}


async def final_report_generator(state: InterviewState):
    final_report = await get_final_report_generator_template().ainvoke(state)
    return {"final_report": final_report}


def finish_interview(state: InterviewState):
    if "interview_completed" in state and state["interview_completed"]:
        return "final_report_generator"
    # TODO: Use constants
    return "subgraph"
