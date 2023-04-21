# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import TYPE_CHECKING
from typing import Literal
import pandas as pd
from .PlotAdapter import PlotAdapter


class Table:
    def __init__(self, data: DefineType.table_data):
        pass


    @property
    def data(self) -> DefineType.table_data:  # type: ignore
        pass

    def set_index(self, columnName: str):
        pass

    def remove_display_limit(self, direction: Literal['row', 'column']):
        pass

    def add_row(self):
        pass

    def add_column(self, columnName:  Union[str , int , float] , body: list[ Union[str , int , float] ]):
        pass

    def display(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
