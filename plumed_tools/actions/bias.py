from typing import Optional
from pydantic import BaseModel
from pydantic import field_validator, validator


class Wall(BaseModel):
    LABEL: Optional[str] = None
    ARG: list[str]
    AT: list[float]
    KAPPA: list[float]
    OFFSET: float = 0.0
    EXP: float = 2.0
    EPS: float = 1.0
    NUMERICAL_DERIVATIVES: bool = False


class UPPER_WALLS(Wall):
    pass


class LOWER_WALLS(Wall):
    pass


class METAD(BaseModel):
    ARG: list[str]
    SIGMA: list[float]
    PACE: int
    FILE: str = "HILLS"
    LABEL: Optional[str] = None

    NUMERICAL_DERIVATIVES: Optional[bool] = False
    CALC_WORK: Optional[bool] = False
    CALC_RCT: Optional[bool] = False
    GRID_SPARSE: Optional[bool] = False
    GRID_NOSPLINE: Optional[bool] = False
    STORE_GRIDS: Optional[bool] = False
    NLIST: Optional[bool] = False
    WALKERS_MPI: Optional[bool] = False
    FLYING_GAUSSIAN: Optional[bool] = False
    ACCELERATION: Optional[bool] = False
    CALC_MAX_BIAS: Optional[bool] = False
    CALC_TRANSITION_BIAS: Optional[bool] = False
    FREQUENCY_ADAPTIVE: Optional[bool] = False
    HEIGHT: Optional[list[float]] = None
    FMT: Optional[str] = None
    BIASFACTOR: Optional[float] = None
    RECT: Optional[list[float]] = None
    DAMPFACTOR: Optional[float] = None
    TTBIASFACTOR: Optional[float] = None
    TTBIASTHRESHOLD: Optional[float] = None
    TTALPHA: Optional[float] = None
    TARGET: Optional[str] = None
    TEMP: Optional[float] = None
    TAU: Optional[float] = None
    RCT_USTRIDE: Optional[int] = None
    GRID_MIN: Optional[list[float]] = None
    GRID_MAX: Optional[list[float]] = None
    GRID_BIN: Optional[list[int]] = None
    GRID_SPACING: Optional[float] = None
    GRID_WSTRIDE: Optional[int] = None
    GRID_WFILE: Optional[str] = None
    GRID_RFILE: Optional[str] = None
    NLIST_PARAMETERS: Optional[list[float]] = None
    ADAPTIVE: Optional[str] = None
    SIGMA_MAX: Optional[float] = None
    SIGMA_MIN: Optional[float] = None
    WALKERS_ID: Optional[int] = None
    WALKERS_N: Optional[int] = None
    WALKERS_DIR: Optional[str] = None
    WALKERS_RSTRIDE: Optional[int] = None
    INTERVAL: Optional[list[float]] = None
    ACCELERATION_RFILE: Optional[str] = None
    TRANSITIONWELL: Optional[list[float]] = None
    FA_UPDATE_FREQUENCY: Optional[int] = None
    FA_MAX_PACE: Optional[int] = None
    FA_MIN_ACCELERATION: Optional[float] = None
    RESTART: Optional[str] = None
    UPDATE_FROM: Optional[float] = None
    UPDATE_UNTIL: Optional[float] = None

    @field_validator('HEIGHT')
    def validate_height(cls, height, values):
        tau = values.get('TAU')
        bias_factor = values.get('BIASFACTOR')
        damp_factor = values.get('DAMPFACTOR')
        if not height and (not tau or not (bias_factor or damp_factor)):
            raise ValueError(
                "HEIGHT is compulsory unless TAU and either BIASFACTOR or DAMPFACTOR are given")
        return height


class OPES_METAD_EXPLORE(BaseModel):
    ARG: list[str]
    LABEL: Optional[str] = None

    TEMP: Optional[float] = -1.0
    PACE: int
    SIGMA: Optional[list[float]] = None
    BARRIER: Optional[float] = None
    COMPRESSION_THRESHOLD: Optional[float] = 1.0
    FILE: Optional[str] = "KERNELS"
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NLIST: Optional[bool] = False
    NLIST_PACE_RESET: Optional[bool] = False
    FIXED_SIGMA: Optional[bool] = False
    RECURSIVE_MERGE_OFF: Optional[bool] = False
    NO_ZED: Optional[bool] = False
    STORE_STATES: Optional[bool] = False
    CALC_WORK: Optional[bool] = False
    WALKERS_MPI: Optional[bool] = False
    SERIAL: Optional[bool] = False
    ADAPTIVE_SIGMA_STRIDE: Optional[int] = None
    SIGMA_MIN: Optional[list[float]] = None
    BIASFACTOR: Optional[float] = None
    EPSILON: Optional[float] = None
    KERNEL_CUTOFF: Optional[float] = None
    NLIST_PARAMETERS: Optional[list[float]] = [3.0, 0.5]
    FMT: Optional[str] = None
    STATE_RFILE: Optional[str] = None
    STATE_WFILE: Optional[str] = None
    STATE_WSTRIDE: Optional[int] = None
    EXCLUDED_REGION: Optional[str] = None
    RESTART: Optional[str] = None
    UPDATE_FROM: Optional[float] = None
    UPDATE_UNTIL: Optional[float] = None


class OPES_METAD(BaseModel):
    ARG: list[str]
    LABEL: Optional[str] = None

    TEMP: Optional[float] = -1.0
    PACE: int
    SIGMA: Optional[list[float]] = None
    BARRIER: Optional[float] = None
    COMPRESSION_THRESHOLD: Optional[float] = 1.0
    FILE: Optional[str] = "KERNELS"
    NUMERICAL_DERIVATIVES: Optional[bool] = False
    NLIST: Optional[bool] = False
    NLIST_PACE_RESET: Optional[bool] = False
    FIXED_SIGMA: Optional[bool] = False
    RECURSIVE_MERGE_OFF: Optional[bool] = False
    NO_ZED: Optional[bool] = False
    STORE_STATES: Optional[bool] = False
    CALC_WORK: Optional[bool] = False
    WALKERS_MPI: Optional[bool] = False
    SERIAL: Optional[bool] = False
    ADAPTIVE_SIGMA_STRIDE: Optional[int] = None
    SIGMA_MIN: Optional[list[float]] = None
    BIASFACTOR: Optional[float] = None
    EPSILON: Optional[float] = None
    KERNEL_CUTOFF: Optional[float] = None
    NLIST_PARAMETERS: Optional[list[float]] = [3.0, 0.5]
    FMT: Optional[str] = None
    STATE_RFILE: Optional[str] = None
    STATE_WFILE: Optional[str] = None
    STATE_WSTRIDE: Optional[int] = None
    EXCLUDED_REGION: Optional[str] = None
    EXTRA_BIAS: Optional[list[str]] = None
    RESTART: Optional[str] = None
    UPDATE_FROM: Optional[float] = None
    UPDATE_UNTIL: Optional[float] = None
