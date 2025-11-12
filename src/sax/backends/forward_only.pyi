from typing import Any

import sax

__all__ = [
    "analyze_circuit_forward",
    "analyze_instances_forward",
    "evaluate_circuit_forward",
]

def analyze_instances_forward(
    instances: sax.Instances, models: sax.Models,
) -> dict[sax.InstanceName, sax.SCoo]: ...
def analyze_circuit_forward(
    analyzed_instances: dict[sax.InstanceName, sax.SDict],
    connections: sax.Connections,
    ports: sax.Ports,
) -> Any: ...
def evaluate_circuit_forward(
    analyzed: Any, instances: dict[str, sax.SDict],
) -> sax.SDict: ...
