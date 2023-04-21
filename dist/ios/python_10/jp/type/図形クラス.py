# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import cast
from typing import TYPE_CHECKING
from .PlotAdapter import FigureBase


class 図形クラス(FigureBase):
    def __init__(self, 証明: 型定義クラス.証明クラス, row_column: tuple[int, int], unit_size: tuple[int | float, int | float] = (5, 5), タイトル: str = ''):
        pass


    @property
    def 証明(self) -> 型定義クラス.証明クラス:  # type: ignore
        pass

    @property
    def 座標ず(self) -> list[list[型定義クラス.座標クラス]]:  # type: ignore
        pass

    def 足す_座標システム(self, row_column: tuple[int, int]) -> 図形クラス:  # type: ignore
        pass

    def 表示する(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
