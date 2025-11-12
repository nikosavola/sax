from sax.saxtypes.core import FloatArray1D

__all__ = [
    "C_M_S",
    "C_UM_S",
    "DEFAULT_MODE",
    "DEFAULT_MODES",
    "DEFAULT_WL_STEP",
    "EPS",
    "WL_C",
    "WL_C_MAX",
    "WL_C_MIN",
    "WL_E",
    "WL_E_MAX",
    "WL_E_MIN",
    "WL_L",
    "WL_L_MAX",
    "WL_L_MIN",
    "WL_O",
    "WL_O_MAX",
    "WL_O_MIN",
    "WL_S",
    "WL_S_MAX",
    "WL_S_MIN",
    "wl_c",
    "wl_e",
    "wl_l",
    "wl_o",
    "wl_s",
]

EPS: float
C_M_S: float
C_UM_S: float
DEFAULT_MODE: str
DEFAULT_MODES: tuple[str, ...]
DEFAULT_WL_STEP: float
WL_O_MIN: float
WL_O_MAX: float
WL_O: float
WL_E_MIN: float
WL_E_MAX: float
WL_E: float
WL_S_MIN: float
WL_S_MAX: float
WL_S: float
WL_C_MIN: float
WL_C_MAX: float
WL_C: float
WL_L_MIN: float
WL_L_MAX: float
WL_L: float

def wl_o(
    *,
    step: float = ...,
    num: int | None = None,
    wl_min: float = ...,
    wl_max: float = ...,
) -> FloatArray1D: ...
def wl_e(
    *,
    step: float = ...,
    num: int | None = None,
    wl_min: float = ...,
    wl_max: float = ...,
) -> FloatArray1D: ...
def wl_s(
    *,
    step: float = ...,
    num: int | None = None,
    wl_min: float = ...,
    wl_max: float = ...,
) -> FloatArray1D: ...
def wl_c(
    *,
    step: float = ...,
    num: int | None = None,
    wl_min: float = ...,
    wl_max: float = ...,
) -> FloatArray1D: ...
def wl_l(
    *,
    step: float = ...,
    num: int | None = None,
    wl_min: float = ...,
    wl_max: float = ...,
) -> FloatArray1D: ...
