from langgraph.graph import START, END, StateGraph
from agent.states.interview_state import InterviewState
from agent.nodes.interview_nodes import (
    process_resume,
    planner,
    replanner,
    feedback_summarizer,
    final_report_generator,
    finish_interview
)

from agent.workflows.step_workflow import interview_step_workflow

def get_main_interview_workflow() -> StateGraph:
    workflow = StateGraph(InterviewState)

    subgraph = interview_step_workflow()

    workflow.add_node(process_resume)
    workflow.add_node(planner)
    workflow.add_node(replanner)
    workflow.add_node(feedback_summarizer)
    workflow.add_node(final_report_generator)
    workflow.add_node("subgraph", subgraph)

    workflow.add_edge(START, process_resume.__name__)
    workflow.add_edge(process_resume.__name__, planner.__name__)
    workflow.add_edge(pla
    , "subgraph")
    workflow.add_edge("subgraph", feedback_summarizer.__name__)
    workflow.add_edge(feedback_summarizer.__name__, replanner.__name__)
    workflow.add_conditional_edges(
        replanner.__name__,
        finish_interview,
        ["subgraph", final_report_generator.__name__],
    )
    workflow.add_edge(final_report_generator.__name__, END)

    workflow = workflow.compile()

    return workflow

if __name__ == "__main__":
    workflow = get_main_interview_workflow()
    print(workflow.get_graph(xray=True).draw_mermaid())