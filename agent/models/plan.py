from pydantic import BaseModel
from typing import List
from agent.models.step import Step


class Plan(BaseModel):
    steps: List[Step]
