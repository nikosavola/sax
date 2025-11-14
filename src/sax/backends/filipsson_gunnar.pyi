from typing import Any

import sax

__all__ = ["analyze_circuit_fg", "analyze_instances_fg", "evaluate_circuit_fg"]

def analyze_instances_fg(
    instances: sax.Instances, models: sax.Models,
) -> dict[sax.InstanceName, sax.SDict]: ...
def analyze_circuit_fg(
    analyzed_instances: dict[str, sax.SDict],
    connections: sax.Connections,
    ports: sax.Ports,
) -> Any: ...
def evaluate_circuit_fg(
    analyzed: Any, instances: dict[str, sax.SType],
) -> sax.SDict: ...
