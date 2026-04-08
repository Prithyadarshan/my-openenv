from pydantic import BaseModel

class Observation(BaseModel):
    email_text: str
    sender: str
    subject: str
    step: int

class Action(BaseModel):
    classification: str
    reply: str
    archive: bool

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict
