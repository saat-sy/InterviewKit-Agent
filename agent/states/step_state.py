from typing_extensions import TypedDict
from typing import List, Tuple
from agent.models.plan import Plan
from agent.models.step import Step
from datetime import datetime

class StepState(TypedDict):
    plan: Plan
    executed_steps: List[Tuple[Step, str]]
    feedback: List[str]
    step_start_time: datetime
    step_completed: bool
    response: List[str]