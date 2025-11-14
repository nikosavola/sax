from pydantic import validate_call

import sax

@validate_call
def model_2port(p1: sax.Name, p2: sax.Name) -> sax.SDictModel: ...
@validate_call
def model_3port(p1: sax.Name, p2: sax.Name, p3: sax.Name) -> sax.SDictModel: ...
@validate_call
def model_4port(
    p1: sax.Name, p2: sax.Name, p3: sax.Name, p4: sax.Name,
) -> sax.SDictModel: ...
@validate_call
def unitary(
    num_inputs: int,
    num_outputs: int,
    *,
    reciprocal: bool = True,
    diagonal: bool = False,
) -> sax.SCooModel: ...
@validate_call
def copier(
    num_inputs: int,
    num_outputs: int,
    *,
    reciprocal: bool = True,
    diagonal: bool = False,
) -> sax.SCooModel: ...
@validate_call
def passthru(num_links: int, *, reciprocal: bool = True) -> sax.SCooModel: ...
