from pydantic import BaseModel


class Boolean(BaseModel):
    value: bool
