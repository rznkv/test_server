from pydantic import BaseModel

class MathRequest(BaseModel):
    digits: list[float]
    action: str
