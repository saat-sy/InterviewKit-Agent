from typing_extensions import TypedDict
from typing import List, Tuple, Annotated
import operator
from agent.models.plan import Plan
from agent.models.step import Step
from datetime import datetime
from dataclasses import dataclass, field

@dataclass
class StepState(TypedDict):
    plan: Plan
    step_start_time: datetime
    step_completed: bool
    duration: int
    executed_steps: Annotated[List[Tuple[Step, str]], operator.add]
    feedback: Annotated[List[str], operator.add]
    response: Annotated[List[Tuple[str, str]], operator.add]
    overall_feedback: Annotated[List[Tuple[Plan, str]], operator.add]