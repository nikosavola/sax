from typing import Any, Literal, overload

import networkx as nx

import sax

__all__ = ["circuit", "draw_dag", "get_required_circuit_models"]

@overload
def circuit(
    netlist: sax.AnyNetlist,
    models: sax.Models | None = None,
    *,
    backend: sax.BackendLike = "default",
    top_level_name: str = "top_level",
    ignore_impossible_connections: bool = False,
) -> tuple[sax.SDictModel, sax.CircuitInfo]: ...
@overload
def circuit(
    netlist: sax.AnyNetlist,
    models: sax.Models | None = None,
    *,
    backend: sax.BackendLike = "default",
    return_type: Literal["SDict"],
    top_level_name: str = "top_level",
    ignore_impossible_connections: bool = False,
) -> tuple[sax.SDictModel, sax.CircuitInfo]: ...
@overload
def circuit(
    netlist: sax.AnyNetlist,
    models: sax.Models | None = None,
    *,
    backend: sax.BackendLike = "default",
    return_type: Literal["SDense"],
    top_level_name: str = "top_level",
    ignore_impossible_connections: bool = False,
) -> tuple[sax.SDenseModel, sax.CircuitInfo]: ...
@overload
def circuit(
    netlist: sax.AnyNetlist,
    models: sax.Models | None = None,
    *,
    backend: sax.BackendLike = "default",
    return_type: Literal["SCoo"],
    top_level_name: str = "top_level",
    ignore_impossible_connections: bool = False,
) -> tuple[sax.SCooModel, sax.CircuitInfo]: ...
def draw_dag(dag: nx.DiGraph, *, with_labels: bool = True, **kwargs: Any) -> None: ...
def get_required_circuit_models(
    netlist: sax.AnyNetlist, models: dict[str, sax.Model] | None = None,
) -> list[str]: ...
