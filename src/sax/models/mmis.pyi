import jax
from pydantic import validate_call

import sax

from .couplers import coupler_ideal as coupler_ideal
from .splitters import splitter_ideal as splitter_ideal

@jax.jit
@validate_call
def mmi1x2_ideal(wl: sax.FloatArrayLike = ...) -> sax.SDict: ...
@jax.jit
@validate_call
def mmi2x2_ideal(*, wl: sax.FloatArrayLike = ...) -> sax.SDict: ...
@jax.jit
@validate_call
def mmi1x2(
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    fwhm: sax.FloatArrayLike = 0.2,
    loss_dB: sax.FloatArrayLike = 0.3,
) -> sax.SDict: ...
@jax.jit
@validate_call
def mmi2x2(
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    fwhm: sax.FloatArrayLike = 0.2,
    loss_dB: sax.FloatArrayLike = 0.3,
    shift: sax.FloatArrayLike = 0.0,
    loss_dB_cross: sax.FloatArrayLike | None = None,
    loss_dB_thru: sax.FloatArrayLike | None = None,
    splitting_ratio_cross: sax.FloatArrayLike = 0.5,
    splitting_ratio_thru: sax.FloatArrayLike = 0.5,
) -> sax.SDict: ...
