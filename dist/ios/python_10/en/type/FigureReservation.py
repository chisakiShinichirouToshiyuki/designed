# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import TYPE_CHECKING


class FigureReservation:
    def __init__(self, express: DefineType.SymbolCondition | DefineType.Formula, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = ''):
        pass


    def display(self):
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
