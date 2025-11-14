import jax

import sax

def gamma_0_load(
    f: sax.FloatArrayLike = ...,
    gamma_0: sax.ComplexLike = 0,
    n_ports: sax.IntLike = 1,
) -> sax.SDict: ...
@jax.jit
def tee(f: sax.FloatArrayLike = ...) -> sax.SDict: ...
@jax.jit
def impedance(
    f: sax.FloatArrayLike, z: sax.ComplexLike = 50, z0: sax.ComplexLike = 50,
) -> sax.SDict: ...
@jax.jit
def admittance(f: sax.FloatArrayLike, y: sax.ComplexLike = ...) -> sax.SDict: ...
def capacitor(
    f: sax.FloatArrayLike = ...,
    capacitance: sax.FloatLike = 1e-15,
    z0: sax.ComplexLike = 50,
) -> sax.SDict: ...
def inductor(
    f: sax.FloatArrayLike = ...,
    inductance: sax.FloatLike = 1e-12,
    z0: sax.ComplexLike = 50,
) -> sax.SDict: ...
