from langgraph.graph import START, END, StateGraph
from agent.states.step_state import StepState
from agent.nodes.step_nodes import (
    technical_agent,
    feedback_from_response,
    finish_step
)

def interview_step_workflow() -> StateGraph:
    workflow = StateGraph(StepState)

    workflow.add_node(technical_agent)
    workflow.add_node(feedback_from_response)

    workflow.add_edge(START, technical_agent.__name__)
    workflow.add_edge(technical_agent.__name__, feedback_from_response.__name__)
    workflow.add_conditional_edges(
        feedback_from_response.__name__,
        finish_step,
        [technical_agent.__name__, END],
    )

    workflow = workflow.compile()
    return workflow

if __name__ == "__main__":
    workflow = interview_step_workflow()
    print(workflow.get_graph().draw_mermaid())