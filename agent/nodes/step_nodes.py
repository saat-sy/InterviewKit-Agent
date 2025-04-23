from agent.states.step_state import StepState

async def technical_agent(state: StepState):
    return {
        "response": state["response"] + "",
    }

async def feedback_from_response(state: StepState):
    return {
        "feedback": state["feedback"] + "",
    }

def finish_step(state: StepState):
    return "technical_agent"