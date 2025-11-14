import jax
from pydantic import validate_call

import sax

@jax.jit
@validate_call
def straight(
    *,
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    neff: sax.FloatArrayLike = 2.34,
    ng: sax.FloatArrayLike = 3.4,
    length: sax.FloatArrayLike = 10.0,
    loss_dB_cm: sax.FloatArrayLike = 0.0,
) -> sax.SDict: ...
@jax.jit
@validate_call
def attenuator(
    *, wl: sax.FloatArrayLike = ..., loss: sax.FloatArrayLike = 0.0,
) -> sax.SDict: ...
@jax.jit
@validate_call
def phase_shifter(
    wl: sax.FloatArrayLike = ...,
    neff: sax.FloatArrayLike = 2.34,
    voltage: sax.FloatArrayLike = 0,
    length: sax.FloatArrayLike = 10,
    loss: sax.FloatArrayLike = 0.0,
) -> sax.SDict: ...
