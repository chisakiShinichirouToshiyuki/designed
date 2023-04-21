# pyright: reportUnusedImport=false
from __future__ import annotations
from matplotlib.ticker import MaxNLocator
from pprint import pprint
from typing import Any, Literal, TYPE_CHECKING, TypedDict
# import FormulaManipulationAdapter as FormulaAdapter
import matplotlib.pyplot as plt
import math
import pandas as pd


class PlotAdapter:
    @staticmethod
    def set_table_index(data_frame: pd.DataFrame, column_name: str | int | float):
        pass

    @staticmethod
    def remove_display_limit(direction: Literal['row', 'column']):
        pass

    @staticmethod
    def add_column(data_frame: pd.DataFrame, columnName: str | int | float, body: list[str | int | float]):
        pass

    @staticmethod
    def display_table(data_frame: pd.DataFrame):
        pass

class Position_only_x(TypedDict, total=True):
    x: int | float | str


class Position_only_y(TypedDict, total=True):
    y: int | float | str


class Position_only(Position_only_x, Position_only_y):
    pass


class Annotation(TypedDict, total=False):
    annotation: str


class Position(Position_only, Annotation):
    pass


class Position_x(Position_only_x, Annotation):
    pass


class Positions_only_x(TypedDict, total=True):
    x: list[int] | list[float] | list[str]


class Positions_only_y(TypedDict, total=True):
    y: list[int | float | str]


class Positions_only(Positions_only_x, Positions_only_y):
    pass


class Annotations(TypedDict, total=False):
    annotation: list[str]


class Positions_list(Positions_only, Annotations):
    pass


class Positions_list_x(Positions_only_x, Annotations):
    pass


class plotRange(TypedDict):
    min: float | int
    max: float | int


plotRanges = dict[str, plotRange]

variable_symbol = Any
variables = dict[str, variable_symbol]


class AxBase:
    def __init__(self, ax: Any):
        pass


class FigureBase:
    def __init__(self, row_column: tuple[int, int], size: tuple[int | float, int | float] = (15, 7.5), title: str = ''):
        pass


    def show(self) -> FigureBase:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import _ad as DefineType
else:
    from . import DefineType_mock_ad
    DefineType = DefineType_mock_ad.DefineType()
