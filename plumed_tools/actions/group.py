from typing import Optional, Union
from pydantic import BaseModel

class VATOM(BaseModel):
    LABEL: str

class COM(VATOM):
    ATOMS: list[int]
    NOPBC: Optional[bool] = False
    MASS: Optional[bool] = False
    PHASES: Optional[bool] = False
    WEIGHTS: Optional[list[float]]
    SET_CHARGE: Optional[float]
    SET_MASS: Optional[float]

class GROUP(BaseModel):
    ATOMS: list[Union[int, VATOM]]
    LABEL: Optional[str] = None
    REMOVE: Optional[list[Union[int, VATOM]]] = None
    SORT: Optional[bool] = False
    UNIQUE: Optional[bool] = False
    NDX_FILE: Optional[str] = None
    NDX_GROUP: Optional[str] = None
