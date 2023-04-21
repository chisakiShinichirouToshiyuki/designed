# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from .PlotAdapter import AxBase
from typing import TYPE_CHECKING
from typing import Literal
from typing import Any


class Ax(AxBase):
    def __init__(self, figure: DefineType.Figure, ax: Any):
        pass


    def plot_line_formula(self, formula: DefineType.Formula | str | float | int | DefineType.NativeFraction, variable: str, color: DefineType.hsla = (220, 100, 50), label: str = '') -> Ax:  # type: ignore
        pass

    def plot_scatter_formula(self, data: list[DefineType.Position_x] | DefineType.Positions_list_x, formula: DefineType.Formula | str | float | int | DefineType.NativeFraction, variable: str, color: DefineType.plot_color | DefineType.hex_rgb = 'black', label: str = '') -> Ax:  # type: ignore
        pass

    def plot_scatter_points(self, data: list[DefineType.Position] | DefineType.Positions_list, color: DefineType.plot_color | DefineType.hex_rgb) -> Ax:  # type: ignore
        pass

    def plot_condition(self, condition: DefineType.SymbolCondition, axises: list[str] | None = None, color: DefineType.hsla | None = None) -> Ax:  # type: ignore
        """
        """
        pass

    def add_grid(self) -> Ax:  # type: ignore
        pass

    def reset_range(self, _range: DefineType.plotRange_2d) -> Ax:  # type: ignore
        """グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        pass

    def reset_title(self, title: str) -> Ax:  # type: ignore
        """グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        pass

    def reset_label(self, labels: tuple[str, str]) -> Ax:  # type: ignore
        pass

    def reset_plot_property(self, property: Literal['dot_radius', 'line_width', 'z_oder'], value: float | int) -> Ax:  # type: ignore
        pass

    def set_legend(self) -> Ax:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
