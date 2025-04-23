from typing_extensions import TypedDict
from typing import List
from agent.models.step import Step
from datetime import datetime

class StepState(TypedDict):
    step: Step
    start_time: datetime
    feedback: List[str]
    response: List[str]