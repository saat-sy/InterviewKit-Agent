from agent.models.question import Question
from agent.states.step_state import StepState
from agent.prompts.step_prompts import (
    get_technical_agent_template,
    get_feedback_from_response_template,
    get_feedback_summarizer_template,
)
from langgraph.types import interrupt
import time


def initialize_step_state(state: StepState):
    if "step_start_time" not in state:
        return {
            "step_start_time": time.time(),
            "executed_steps": [],
            "feedback": [],
            "response": [],
        }
    return {}


async def technical_agent(state: StepState):
    response: Question = await get_technical_agent_template().ainvoke(
        {
            **state,
            "planned_steps": "\n".join(
                [
                    f"{i+1}. {step.action}: {step.description}"
                    for i, step in enumerate(state["plan"].steps)
                ]
            ),
            "current_plan_name": state["plan"].steps[0].action,
            "current_plan_description": state["plan"].steps[0].description,
            "current_plan_duration": state["plan"].steps[0].duration,
            "elapsed_time": time.strftime(
                "%H:%M:%S", time.gmtime(time.time() - state["step_start_time"])
            ),
        }
    )
    print(response)
    if response.continue_interview:
        answer = interrupt(
            {
                "question": response.question,
            }
        )
        return {"response": [(response.question, answer)]}
    else:
        return {
            "step_completed": True,
        }


async def feedback_from_response(state: StepState):
    response = await get_feedback_from_response_template().ainvoke(
        {
            "response": state["response"][-1],
        }
    )
    return {
        "feedback": [response.response],
    }


async def feedback_summarizer(state: StepState):
    response = await get_feedback_summarizer_template().ainvoke(state)
    return {
        "overall_feedback": [(state["plan"].steps[0], response.response)],
    }


def finish_step(state: StepState):
    if "step_completed" in state and state["step_completed"]:
        return "feedback_summarizer"
    return "technical_agent"
