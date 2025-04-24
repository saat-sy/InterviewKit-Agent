from pydantic import BaseModel, Field
from agent.models.boolean import Boolean
from agent.models.question import Question
from typing import Union

class TechnicalAgentResponse(BaseModel):
    next_steps: Union[Question, Boolean] = Field(
        description="Provide a Question if you are not satisfied with this step, otherwise return Boolean.",
    )