from typing import Optional
from pydantic import BaseModel

class PRINT(BaseModel):
    STRIDE: int = 1
    ARG: Optional[list[str]]
    FILE: Optional[str]
    FMT: Optional[str]
    RESTART: Optional[str]
    UPDATE_FROM: Optional[int]
    UPDATE_TO: Optional[int]
