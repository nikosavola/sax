from typing import Any

import sax

__all__ = ["analyze_circuit_klu", "analyze_instances_klu", "evaluate_circuit_klu"]

def analyze_instances_klu(
    instances: dict[sax.InstanceName, sax.Instance], models: dict[str, sax.Model],
) -> dict[str, sax.SCoo]: ...
def analyze_circuit_klu(
    analyzed_instances: dict[sax.InstanceName, sax.SCoo],
    connections: sax.Connections,
    ports: sax.Ports,
) -> Any: ...
def evaluate_circuit_klu(
    analyzed: Any, instances: dict[sax.InstanceName, sax.SType],
) -> sax.SDense: ...
