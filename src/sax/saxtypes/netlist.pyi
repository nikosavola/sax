from typing import TypeAlias

from _typeshed import Incomplete

from sax.saxtypes.singlemode import InstanceName, InstancePort

__all__ = [
    "AnyNetlist",
    "Component",
    "Connections",
    "Instance",
    "Instances",
    "Net",
    "Netlist",
    "Nets",
    "Placement",
    "Placements",
    "Ports",
    "RecursiveNetlist",
    "default_placement",
]

Component: TypeAlias
Instance: Incomplete
Instances: TypeAlias = dict[InstanceName, Instance]
Placement: Incomplete
Placements: TypeAlias = dict[InstanceName, Placement]
default_placement: Placement
Connections: TypeAlias = dict[InstancePort, InstancePort]
Ports: TypeAlias
Net: Incomplete
Nets: TypeAlias = list[Net]
Netlist: Incomplete
RecursiveNetlist: TypeAlias
AnyNetlist: TypeAlias = Netlist | RecursiveNetlist | dict[str, dict[str, str]]
