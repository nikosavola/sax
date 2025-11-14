from collections.abc import Callable

import sax

from .additive import (
    analyze_circuit_additive as analyze_circuit_additive,
)
from .additive import (
    analyze_instances_additive as analyze_instances_additive,
)
from .additive import (
    evaluate_circuit_additive as evaluate_circuit_additive,
)
from .filipsson_gunnar import (
    analyze_circuit_fg as analyze_circuit_fg,
)
from .filipsson_gunnar import (
    analyze_instances_fg as analyze_instances_fg,
)
from .filipsson_gunnar import (
    evaluate_circuit_fg as evaluate_circuit_fg,
)
from .forward_only import (
    analyze_circuit_forward as analyze_circuit_forward,
)
from .forward_only import (
    analyze_instances_forward as analyze_instances_forward,
)
from .forward_only import (
    evaluate_circuit_forward as evaluate_circuit_forward,
)
from .klu import analyze_circuit_klu, analyze_instances_klu, evaluate_circuit_klu

__all__ = [
    "analyze_circuit",
    "analyze_circuit_additive",
    "analyze_circuit_fg",
    "analyze_circuit_forward",
    "analyze_instances",
    "analyze_instances_additive",
    "analyze_instances_fg",
    "analyze_instances_forward",
    "circuit_backends",
    "evaluate_circuit",
    "evaluate_circuit_additive",
    "evaluate_circuit_fg",
    "evaluate_circuit_forward",
]

circuit_backends: dict[sax.Backend, tuple[Callable, Callable, Callable]]
analyze_instances = analyze_instances_klu
analyze_circuit = analyze_circuit_klu
evaluate_circuit = evaluate_circuit_klu
analyze_instances = analyze_instances_fg
analyze_circuit = analyze_circuit_fg
evaluate_circuit = evaluate_circuit_fg
