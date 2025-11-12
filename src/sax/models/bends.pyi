import jax
from pydantic import validate_call

import sax

from .straight import straight as straight

@jax.jit
@validate_call
def bend(
    wl: sax.FloatArrayLike = ...,
    wl0: sax.FloatArrayLike = ...,
    neff: sax.FloatArrayLike = 2.34,
    ng: sax.FloatArrayLike = 3.4,
    length: sax.FloatArrayLike = 10.0,
    loss_dB_cm: sax.FloatArrayLike = 0.1,
) -> sax.SDict: ...
