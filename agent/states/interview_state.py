from typing_extensions import TypedDict
from typing import List, Tuple, Annotated
import operator
from agent.models.plan import Plan
from agent.models.step import Step
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class InterviewState(TypedDict):
    raw_resume: str
    raw_job_description: str
    processed_resume: str
    duration: int
    interview_start_time: datetime
    plan: Plan
    interview_completed: bool
    final_report: str
    executed_steps: Annotated[List[Tuple[Step, str]], operator.add]
    overall_feedback: Annotated[List[Tuple[Plan, str]], operator.add]
