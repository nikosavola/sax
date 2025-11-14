from pathlib import Path
from typing import overload

import numpy as np
import pandas as pd
from lark import Token as Token
from lark import Transformer
from numpy.typing import NDArray as NDArray
from typing_extensions import TypedDict

import sax

def parse_lumerical_dat(
    content_or_filename: str | Path | sax.IOLike, *, convert_f_to_wl: bool = False,
) -> pd.DataFrame: ...
@overload
def write_lumerical_dat(df: pd.DataFrame, path: None) -> str: ...
@overload
def write_lumerical_dat(df: pd.DataFrame, path: str | Path) -> Path: ...

class _SparamsTransformer(Transformer):
    def start(
        self, header: str, *datablocks: pd.DataFrame,
    ) -> tuple[str, pd.DataFrame]: ...
    def datablock(
        self, ports: _PortsDict, shape: tuple[int, int], values: NDArray[np.float64],
    ) -> pd.DataFrame: ...
    def ports(
        self,
        port_out: str,
        mode_type: str,
        mode_out: int,
        port_in: str,
        mode_in: int,
        valuetype: str,
        groupdelay: str | None = None,
        sweepparams: str | None = None,
    ) -> _PortsDict: ...
    def shape(self, args: list[Token]) -> tuple[int, int]: ...
    def values(self, args: list[NDArray[np.float64]]) -> np.ndarray: ...
    def row(self, args: list[Token]) -> np.ndarray: ...
    def port(self, port: Token) -> str: ...
    def modeid(self, mid: Token) -> int: ...
    def sweepparams(self, params: Token) -> list[str]: ...
    def MODE(self, args: Token) -> str: ...
    def VALUETYPE(self, args: Token) -> str: ...
    def INT(self, args: Token) -> int: ...
    def STRING(self, args: Token) -> str: ...

class _PortsDict(TypedDict):
    port_out: str
    mode_type: str
    mode_out: int
    port_in: str
    mode_in: int
    valuetype: str
    groupdelay: float | None
    sweepparams: str | None
