# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import TYPE_CHECKING
from typing import Literal
import pandas as pd
from .PlotAdapter import PlotAdapter


class テーブルクラス:
    def __init__(self, data: 型定義クラス.テーブルdata):
        pass


    @property
    def data(self) -> 型定義クラス.テーブルdata:  # type: ignore
        pass

    def 設定する_index(self, 列名: str):
        pass

    def 解除する_表示上限(self, 方向: Literal['row', 'column']):
        pass

    def 足す_行(self):
        pass

    def 足す_列(self, 列名:  Union[str , int , float] , ボディ: list[ Union[str , int , float] ]):
        pass

    def 表示する(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
