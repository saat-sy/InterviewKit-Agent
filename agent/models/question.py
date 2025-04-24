from pydantic import BaseModel


class Question(BaseModel):
    question: str
    continue_interview: bool
