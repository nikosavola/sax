from typing import TypeAlias, TypeVar

from .core import ComplexArray, IntArray1D, Name

__all__ = [
    "InstanceName",
    "InstancePort",
    "ModelFactorySM",
    "ModelSM",
    "ModelsSM",
    "Port",
    "PortCombinationSM",
    "PortMapSM",
    "SCooModelFactorySM",
    "SCooModelSM",
    "SCooSM",
    "SDenseModelFactorySM",
    "SDenseModelSM",
    "SDenseSM",
    "SDictModelFactorySM",
    "SDictModelSM",
    "SDictSM",
    "STypeSM",
]

T = TypeVar("T")
InstanceName: TypeAlias
Port: TypeAlias
InstancePort: TypeAlias
PortMapSM: TypeAlias = dict[Port, int]
PortCombinationSM: TypeAlias = tuple[Port, Port]
SDictSM: TypeAlias = dict[PortCombinationSM, ComplexArray]
SDenseSM: TypeAlias = tuple[ComplexArray, PortMapSM]
SCooSM: TypeAlias = tuple[IntArray1D, IntArray1D, ComplexArray, PortMapSM]
STypeSM: TypeAlias = SDictSM | SCooSM | SDenseSM
SDictModelSM: TypeAlias
SDenseModelSM: TypeAlias
SCooModelSM: TypeAlias
ModelSM: TypeAlias
SDictModelFactorySM: TypeAlias
SDenseModelFactorySM: TypeAlias
SCooModelFactorySM: TypeAlias
ModelFactorySM: TypeAlias
ModelsSM: TypeAlias = dict[Name, ModelSM]
