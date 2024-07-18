from typing import Any, Optional
from pydantic import BaseModel
from pydantic import field_validator

from plumed_tools.actions.group import GROUP

class DISTANCE(BaseModel):
    ATOMS: GROUP
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NOPBC: Optional[bool] = False
    COMPONENTS: Optional[bool] = False
    SCALED_COMPONENTS: Optional[bool] = False

    @field_validator("ATOMS")
    @classmethod
    def check_atoms(cls, v: Any):
        if len(v.ATOMS) != 2:
            raise ValueError("ATOMS must have exactly 2 elements")
        return v

class ANGLE(BaseModel):
    ATOMS: GROUP
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NOPBC: Optional[bool] = False

    @field_validator("ATOMS")
    @classmethod
    def check_atoms(cls, v: Any):
        if len(v.ATOMS) != 3:
            raise ValueError("ATOMS must have exactly 3 elements")
        return v

class TORSION(BaseModel):
    class TORSION_VECTOR(BaseModel):
        AXIS: GROUP
        VECTOR1: GROUP
        VECTOR2: GROUP

    ATOMS: Optional[GROUP] = None
    VECTOR: Optional[TORSION_VECTOR] = None
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NOPBC: Optional[bool] = False

    @field_validator("ATOMS")
    @classmethod
    def check_atoms(cls, v: Any):
        if v is None and cls.VECTOR is None:
            raise ValueError("Either ATOMS or VECTOR must be provided")
        if v is not None and cls.ATOMS is not None:
            raise ValueError("Only one of ATOMS or VECTOR should be provided")
        if len(v.ATOMS) != 4:
            raise ValueError("ATOMS must have exactly 4 elements")
        return v
    
    @field_validator("VECTOR")
    @classmethod
    def check_vector(cls, v: Any):
        if v is None and cls.ATOMS is None:
            raise ValueError("Either ATOMS or VECTOR must be provided")
        if v is not None and cls.ATOMS is not None:
            raise ValueError("Only one of ATOMS or VECTOR should be provided")
        return v

class COORDINATION(BaseModel):
    GROUPA: GROUP
    GROUPB: GROUP
    NN: int = 6
    MM: int = 0
    D_0: float= 0.0
    R_0: Optional[float]
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NOPBC: Optional[bool] = False
