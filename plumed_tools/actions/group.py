from typing import Optional, Union
from pydantic import BaseModel

class Labeled(BaseModel):
    LABEL: Optional[str] = None

    def __str__(self) -> str:
        return self.LABEL

class COM(Labeled):
    ATOMS: list[Union[int, Labeled]]
    NOPBC: Optional[bool] = False
    MASS: Optional[bool] = False
    PHASES: Optional[bool] = False
    WEIGHTS: Optional[list[float]] = None
    SET_CHARGE: Optional[float] = None
    SET_MASS: Optional[float] = None

class GROUP(Labeled):
    ATOMS: list[Union[int, Labeled]]
    REMOVE: Optional[list[Union[int, Labeled]]] = None
    SORT: Optional[bool] = False
    UNIQUE: Optional[bool] = False
    NDX_FILE: Optional[str] = None
    NDX_GROUP: Optional[str] = None
