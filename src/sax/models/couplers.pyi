import jax
from pydantic import validate_call

import sax

@jax.jit
@validate_call
def coupler_ideal(
    *, wl: sax.FloatArrayLike = ..., coupling: sax.FloatArrayLike = 0.5,
) -> sax.SDict: ...
@jax.jit
@validate_call
def coupler(
    *,
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    length: sax.FloatArrayLike = 0.0,
    coupling0: sax.FloatArrayLike = 0.2,
    dk1: sax.FloatArrayLike = 1.2435,
    dk2: sax.FloatArrayLike = 5.3022,
    dn: sax.FloatArrayLike = 0.02,
    dn1: sax.FloatArrayLike = 0.1169,
    dn2: sax.FloatArrayLike = 0.4821,
) -> sax.SDict: ...
@jax.jit
@validate_call
def grating_coupler(
    *,
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    loss: sax.FloatArrayLike = 0.0,
    reflection: sax.FloatArrayLike = 0.0,
    reflection_fiber: sax.FloatArrayLike = 0.0,
    bandwidth: sax.FloatArrayLike = 0.04,
) -> sax.SDict: ...
