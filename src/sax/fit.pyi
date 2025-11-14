from collections.abc import Callable
from pathlib import Path
from typing import TypeAlias

import pandas as pd
from jaxtyping import Array
from typing_extensions import TypedDict

import sax

__all__ = [
    "NeuralFitResult",
    "PRNGKey",
    "Params",
    "neural_fit",
    "neural_fit_equations",
    "write_neural_fit_functions",
]

def neural_fit(
    data: pd.DataFrame,
    targets: list[str],
    features: list[str] | None = None,
    hidden_dims: tuple[int, ...] = (10,),
    learning_rate: float = 0.003,
    num_epochs: int = 1000,
    random_seed: int = 42,
    *,
    activation_fn: Callable = ...,
    loss_fn: Callable = ...,
    progress_bar: bool = True,
) -> NeuralFitResult: ...
def neural_fit_equations(result: NeuralFitResult) -> dict[str, Equation]: ...
def write_neural_fit_functions(
    result: NeuralFitResult, *, with_imports: bool = True, path: Path | None = None,
) -> None: ...

PRNGKey: TypeAlias

class Params(TypedDict):
    w: Array
    b: Array

class NeuralFitResult(TypedDict):
    params: list[Params]
    features: list[str]
    targets: list[str]
    hidden_dims: tuple[int, ...]
    forward_fn: Callable
    predict_fn: Callable
    activation_fn: Callable
    X_norm: sax.Normalization
    Y_norm: sax.Normalization
    learning_rate: float
    num_epochs: int
    final_loss: float

# Names in __all__ with no definition:
#   NeuralFitResult
#   Params
