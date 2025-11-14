import jax
from pydantic import validate_call

import sax

@jax.jit
@validate_call
def crossing_ideal(wl: sax.FloatArrayLike = ...) -> sax.SDict: ...
