from typing_extensions import TypedDict
from typing import List, Tuple
from agent.models.plan import Plan
from agent.models.step import Step
from datetime import datetime

class InterviewState(TypedDict):
    raw_resume: str
    raw_job_description: str
    processed_resume: str
    duration: int
    interview_start_time: datetime
    plan: Plan
    executed_steps: List[Tuple[Step, str]]
    feedback: List[str]
    interview_completed: bool
    final_report: str
