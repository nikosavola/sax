from typing import Any

import sax

__all__ = [
    "analyze_circuit_additive",
    "analyze_instances_additive",
    "evaluate_circuit_additive",
]

def analyze_instances_additive(
    instances: sax.Instances, models: sax.Models,
) -> dict[sax.InstanceName, sax.SDict]: ...
def analyze_circuit_additive(
    analyzed_instances: dict[sax.InstanceName, sax.SDict],
    connections: sax.Connections,
    ports: sax.Ports,
) -> Any: ...
def evaluate_circuit_additive(
    analyzed: Any, instances: dict[sax.InstanceName, sax.SDict],
) -> sax.SDict: ...
