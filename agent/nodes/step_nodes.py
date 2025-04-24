from agent.models.question import Question
from agent.states.step_state import StepState
from agent.prompts.step_prompts import (
    get_technical_agent_template,
    get_feedback_from_response_template,
)
from langgraph.graph import END
import time

async def technical_agent(state: StepState):
    response = await get_technical_agent_template().ainvoke(
        {
            **state,
            "planned_steps": '\n'.join([f"{i+1}. {step.name}: {step.description}" for i, step in enumerate(state["plan"])]),
            "current_plan_name": state["plan"][0].name,
            "current_plan_description": state["plan"][0].description,
            "current_plan_duration": state["plan"][0].duration,
            "elapsed_time": time.strftime("%H:%M:%S", time.gmtime(time.time() - state["step_start_time"]))
        }
    )

    if isinstance(response, Question):
        pass
    else:
        return {
            "step_completed": response
        }

    return {
        "response": state["response"] + "",
    }

async def feedback_from_response(state: StepState):
    response = await get_feedback_from_response_template().ainvoke(state)
    return {
        "feedback": state["feedback"] + response,
    }

def finish_step(state: StepState):
    if "step_completed" in state and state["step_completed"]:
        return END
    return "technical_agent"