from collections.abc import Iterable
from pathlib import Path
from typing import overload

import pandas as pd

__all__ = ["parse_touchstone", "write_touchstone"]

def parse_touchstone(
    content_or_filename: str | Path,
    *,
    ports: Iterable[str] = (),
    convert_to_wavelength: bool = True,
) -> pd.DataFrame: ...
@overload
def write_touchstone(df: pd.DataFrame, path: None) -> str: ...
@overload
def write_touchstone(df: pd.DataFrame, path: str | Path) -> Path: ...
