from typing import Union
from pydantic import BaseModel, Field
from agent.models.plan import Plan

class Replan(BaseModel):
    action: Union[Plan, bool] = Field(
        description="The action to be taken. If you want the interview to be over, set this to True."
        "If there are more steps that you want to execute, use Plan",
    )