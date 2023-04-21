# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import TYPE_CHECKING


class 図形登録クラス:
    def __init__(self, 表現形:  Union[型定義クラス.数理的条件クラス , 型定義クラス.式クラス] , 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None] , アルファベット順: bool = True, タイトル: str = ''):
        pass


    def 表示する(self):
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
