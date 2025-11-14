from collections.abc import Callable
from pathlib import Path
from typing import Any, NamedTuple, TypeVar, overload

import sax

from .s import reciprocal as reciprocal

__all__ = [
    "clean_string",
    "copy_settings",
    "flatten_dict",
    "get_settings",
    "grouped_interp",
    "hash_dict",
    "load_netlist",
    "load_recursive_netlist",
    "maybe",
    "merge_dicts",
    "read",
    "reciprocal",
    "rename_params",
    "rename_ports",
    "replace_kwargs",
    "same_args_as",
    "unflatten_dict",
    "update_settings",
]

T = TypeVar("T")

def maybe(
    func: Callable[..., T], /, exc: type[Exception] = ...,
) -> Callable[..., T | None]: ...
def copy_settings(settings: sax.Settings) -> sax.Settings: ...
def read(content_or_filename: str | Path | sax.IOLike) -> str: ...
def load_netlist(content_or_filename: str | Path | sax.IOLike) -> sax.Netlist: ...
def load_recursive_netlist(
    top_level_path: str | Path, ext: str = ".pic.yml",
) -> sax.RecursiveNetlist: ...
def clean_string(
    s: str, dot: str = "p", minus: str = "m", other: str = "_",
) -> sax.Name: ...
def get_settings(model: sax.Model | sax.ModelFactory) -> sax.Settings: ...
def merge_dicts(*dicts: dict) -> dict: ...
def replace_kwargs(func: Callable, **kwargs: sax.SettingsValue) -> None: ...
def update_settings(
    settings: sax.Settings, *compnames: str, **kwargs: sax.SettingsValue,
) -> sax.Settings: ...
def flatten_dict(dic: dict[str, Any], sep: str = ",") -> dict[str, Any]: ...
def unflatten_dict(dic: dict[str, Any], sep: str = ",") -> dict[str, Any]: ...
def grouped_interp(
    wl: sax.FloatArray, wls: sax.FloatArray, phis: sax.FloatArray,
) -> sax.FloatArray: ...
def rename_params(model: sax.Model, renamings: dict[str, str]) -> sax.Model: ...
@overload
def rename_ports(S: sax.SDict, renamings: dict[str, str]) -> sax.SDict: ...
@overload
def rename_ports(S: sax.SCoo, renamings: dict[str, str]) -> sax.SCoo: ...
@overload
def rename_ports(S: sax.SDense, renamings: dict[str, str]) -> sax.SDense: ...
@overload
def rename_ports(S: sax.Model, renamings: dict[str, str]) -> sax.Model: ...
def hash_dict(dic: dict) -> int: ...

class Normalization(NamedTuple):
    mean: sax.ComplexArray
    std: sax.ComplexArray

def same_args_as(
    func: Callable[..., T],
) -> Callable[[Callable[..., T]], Callable[..., T]]: ...
