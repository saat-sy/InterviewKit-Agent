from langgraph.graph import START, END, StateGraph
from agent.states.interview_state import InterviewState
from agent.nodes.interview_nodes import (
    process_resume,
    planner,
    replanner,
    final_report_generator,
    finish_interview,
)

from agent.workflows.step_workflow import interview_step_workflow
from dotenv import load_dotenv

load_dotenv()

workflow = StateGraph(InterviewState)

subgraph = interview_step_workflow()

workflow.add_node(process_resume)
workflow.add_node(planner)
workflow.add_node(replanner)
workflow.add_node(final_report_generator)
workflow.add_node("subgraph", subgraph)

workflow.add_edge(START, process_resume.__name__)
workflow.add_edge(process_resume.__name__, planner.__name__)
workflow.add_edge(planner.__name__, "subgraph")
workflow.add_edge("subgraph", replanner.__name__)
workflow.add_conditional_edges(
    replanner.__name__,
    finish_interview,
    ["subgraph", final_report_generator.__name__],
)
workflow.add_edge(final_report_generator.__name__, END)

graph = workflow.compile()
