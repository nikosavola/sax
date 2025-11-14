import jax
from pydantic import validate_call

import sax

@jax.jit
@validate_call
def splitter_ideal(
    *, wl: sax.FloatArrayLike = ..., coupling: sax.FloatArrayLike = 0.5,
) -> sax.SDict: ...
