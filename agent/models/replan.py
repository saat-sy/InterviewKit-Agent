from pydantic import BaseModel
from agent.models.plan import Plan


class Replan(BaseModel):
    plan: Plan
    step_completed: bool
