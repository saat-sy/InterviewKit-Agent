from agent.models.question import Question
from agent.models.technical_agent_response import TechnicalAgentResponse
from agent.states.step_state import StepState
from agent.prompts.step_prompts import (
    get_technical_agent_template,
    get_feedback_from_response_template,
)
from langgraph.graph import END
from langgraph.types import interrupt
import time

def initialize_step_state(state: StepState):
    if "step_start_time" not in state:
        return {
            "step_start_time": time.time(),
            "executed_steps": [],
            "feedback": [],
            "response": []
        }
    return {}

async def technical_agent(state: StepState):
    response: TechnicalAgentResponse = await get_technical_agent_template().ainvoke(
        {
            **state,
            "planned_steps": '\n'.join([f"{i+1}. {step.action}: {step.description}" for i, step in enumerate(state["plan"].steps)]),
            "current_plan_name": state["plan"].steps[0].action,
            "current_plan_description": state["plan"].steps[0].description,
            "current_plan_duration": state["plan"].steps[0].duration,
            "elapsed_time": time.strftime("%H:%M:%S", time.gmtime(time.time() - state["step_start_time"]))
        }
    )
    print(response)
    if isinstance(response.next_steps, Question):
        answer = interrupt({
            "question": response.next_steps.question,
        })
        print(answer)
        state["response"].append((response.next_steps.question, answer))
        return {
            "response": state["response"]
        }
    else:
        return {
            "step_completed": response.next_steps.value,
        }

async def feedback_from_response(state: StepState):
    response = await get_feedback_from_response_template().ainvoke(state)
    return {
        "feedback": state["feedback"],
    }

def finish_step(state: StepState):
    if "step_completed" in state and state["step_completed"]:
        return END
    return "technical_agent"