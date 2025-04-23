from typing_extensions import TypedDict
from typing import List
from agent.models.plan import Plan

class InterviewState(TypedDict):
    raw_resume: str
    raw_job_description: str
    processed_resume: str
    feedback: List[str]
    final_report: str
    plan: Plan
