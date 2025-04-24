from langgraph.graph import START, END, StateGraph
from agent.states.step_state import StepState
from agent.nodes.step_nodes import (
    initialize_step_state,
    technical_agent,
    feedback_from_response,
    feedback_summarizer,
    finish_step,
)


def interview_step_workflow() -> StateGraph:
    workflow = StateGraph(StepState)

    workflow.add_node(initialize_step_state)
    workflow.add_node(technical_agent)
    workflow.add_node(feedback_from_response)
    workflow.add_node(feedback_summarizer)

    workflow.add_edge(START, initialize_step_state.__name__)
    workflow.add_edge(initialize_step_state.__name__, technical_agent.__name__)
    workflow.add_edge(technical_agent.__name__, feedback_from_response.__name__)
    workflow.add_conditional_edges(
        feedback_from_response.__name__,
        finish_step,
        path_map=[technical_agent.__name__, feedback_summarizer.__name__],
    )

    workflow = workflow.compile()
    return workflow
