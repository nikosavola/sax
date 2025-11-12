from typing import Protocol, TypeAlias, TypeVar

import numpy as np
from jaxtyping import Array

__all__ = [
    "ArrayLike",
    "Bool",
    "BoolArray",
    "BoolArrayLike",
    "BoolLike",
    "Complex",
    "ComplexArray",
    "ComplexArray1D",
    "ComplexArray1DLike",
    "ComplexArrayLike",
    "ComplexLike",
    "Float",
    "FloatArray",
    "FloatArray1D",
    "FloatArray1DLike",
    "FloatArray2D",
    "FloatArray2DLike",
    "FloatArrayLike",
    "FloatLike",
    "IOLike",
    "Int",
    "IntArray",
    "IntArray1D",
    "IntArray1DLike",
    "IntArrayLike",
    "IntLike",
]

T = TypeVar("T")
ArrayLike: TypeAlias = Array | np.ndarray
Bool: TypeAlias
Int: TypeAlias
Float: TypeAlias
Complex: TypeAlias
BoolArray: TypeAlias
IntArray: TypeAlias
FloatArray: TypeAlias
ComplexArray: TypeAlias
IntArray1D: TypeAlias
FloatArray1D: TypeAlias
FloatArray2D: TypeAlias
ComplexArray1D: TypeAlias
BoolLike: TypeAlias
IntLike: TypeAlias
FloatLike: TypeAlias
ComplexLike: TypeAlias
BoolArrayLike: TypeAlias
IntArrayLike: TypeAlias
FloatArrayLike: TypeAlias
ComplexArrayLike: TypeAlias
IntArray1DLike: TypeAlias
FloatArray1DLike: TypeAlias
FloatArray2DLike: TypeAlias
ComplexArray1DLike: TypeAlias

class IOLike(Protocol):
    def read(self, size: int | None = -1, /) -> str: ...
