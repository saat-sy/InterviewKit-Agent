from typing_extensions import TypedDict
from typing import List, Tuple
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
    executed_steps: List[Tuple[Step, str]] = field(default_factory=list)
    feedback: List[str] = field(default_factory=list)
    response: List[Tuple[str, str]] = field(default_factory=list)