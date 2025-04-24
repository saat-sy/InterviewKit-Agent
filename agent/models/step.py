from pydantic import BaseModel


class Step(BaseModel):
    action: str
    description: str
    duration: int
