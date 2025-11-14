from typing import TypeAlias

from .core import ComplexArray, IntArray1D, Name

__all__ = [
    "ModelFactoryMM",
    "ModelMM",
    "ModelsMM",
    "PortCombinationMM",
    "PortMapMM",
    "PortMode",
    "SCooMM",
    "SCooModelFactoryMM",
    "SCooModelMM",
    "SDenseMM",
    "SDenseModelFactoryMM",
    "SDenseModelMM",
    "SDictMM",
    "SDictModelFactoryMM",
    "SDictModelMM",
    "STypeMM",
]

PortMode: TypeAlias
PortMapMM: TypeAlias = dict[PortMode, int]
PortCombinationMM: TypeAlias = tuple[PortMode, PortMode]
SDictMM: TypeAlias = dict[PortCombinationMM, ComplexArray]
SDenseMM: TypeAlias = tuple[ComplexArray, PortMapMM]
SCooMM: TypeAlias = tuple[IntArray1D, IntArray1D, ComplexArray, PortMapMM]
STypeMM: TypeAlias = SDictMM | SCooMM | SDenseMM
SDictModelMM: TypeAlias
SDenseModelMM: TypeAlias
SCooModelMM: TypeAlias
ModelMM: TypeAlias
SDictModelFactoryMM: TypeAlias
SDenseModelFactoryMM: TypeAlias
SCooModelFactoryMM: TypeAlias
ModelFactoryMM: TypeAlias
ModelsMM: TypeAlias = dict[Name, ModelMM]
