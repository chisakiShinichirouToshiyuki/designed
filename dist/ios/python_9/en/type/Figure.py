# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import cast
from typing import TYPE_CHECKING
from .PlotAdapter import FigureBase


class Figure(FigureBase):
    def __init__(self, proof: DefineType.Proof, row_column: tuple[int, int], unit_size: tuple[ Union[int , float] ,  Union[int , float] ] = (5, 5), title: str = ''):
        pass


    @property
    def proof(self) -> DefineType.Proof:  # type: ignore
        pass

    @property
    def axes(self) -> list[list[DefineType.Ax]]:  # type: ignore
        pass

    def add_subplot(self, row_column: tuple[int, int]) -> Figure:  # type: ignore
        pass

    def display(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
