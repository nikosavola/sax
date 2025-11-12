from collections.abc import Iterable

import pandas as pd
import xarray as xr

import sax

__all__ = ["interpolate_xarray", "to_df", "to_xarray"]

def interpolate_xarray(
    xarr: xr.DataArray, /, **kwargs: sax.FloatArray | str,
) -> dict[str, sax.FloatArray]: ...
def to_xarray(
    stacked_data: pd.DataFrame, *, target_names: Iterable[str] = ("amp", "phi"),
) -> xr.DataArray: ...
def to_df(
    obj: xr.DataArray | sax.SType,
    *,
    target_name: str = "target",
    **kwargs: sax.ArrayLike,
) -> pd.DataFrame: ...
