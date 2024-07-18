from typing import Optional
from pydantic import BaseModel

class UNITS(BaseModel):
    NATURAL: Optional[bool] = False
    LENGTH: Optional[str] = "nm"
    ENERGY: Optional[str] = "kj/mol"
    MASS: Optional[str] = "amu"
    TIME: Optional[str] = "ps"
    CHARGE: Optional[str] = "e"
