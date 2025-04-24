from pydantic import BaseModel, Field
from agent.models.question import Question
from typing import Union

class TechnicalAgentResponse(BaseModel):
    next_steps: Union[Question, bool] = Field(
        description="Provide a Question if you are not satisfied with this step, otherwise return True.",
    )