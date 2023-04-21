# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
import inspect
from collections.abc import Callable
from IPython.display import Markdown, Math  # type: ignore
from typing import cast
from typing import TYPE_CHECKING
import re
from typing import overload


class Utils:
    @staticmethod
    def 表示する(contents:  Union[str , Markdown] ) -> None:  # type: ignore
        pass

    @staticmethod
    def getPrimes(range: tuple[int, int]) -> list[int]:  # type: ignore
        pass



    @staticmethod
    @overload
    def euclideanAlgorithm(証明: 型定義クラス.証明クラス, terms: tuple[int, int], 章タイトル: str) -> tuple[int, int]:  # type: ignore
        ...

    @staticmethod
    @overload
    def euclideanAlgorithm(証明: 型定義クラス.証明クラス, terms: tuple[str, str], 章タイトル: str) -> tuple[str, str]:  # type: ignore
        ...

    @staticmethod
    def euclideanAlgorithm(証明: 型定義クラス.証明クラス, terms: tuple[str, str] | tuple[int, int], 章タイトル: str = 'euclideanAlgorithm') -> tuple[int, int] | tuple[str, str]:  # type: ignore
        pass

    @staticmethod
    def cast(証明: 型定義クラス.証明クラス, type: 型定義クラス.term_type, テキスト: str) ->  Union[型定義クラス.整数クラス , 型定義クラス.有限小数クラス , 型定義クラス.分数クラス , 型定義クラス.式クラス] :  # type: ignore
        pass

    @staticmethod
    def 変換できるか(type: 型定義クラス.term_type, テキスト: str) -> bool:  # type: ignore
        pass

    @staticmethod
    def get_called_location() -> int:  # type: ignore
        """関数の呼び出し元の行番号を取得 
        注意:
            !呼び出し元の上位行がすべて空の場合、常に1を返してしまうbugありTODO:修正!

        結果: 
            呼び出し元の行
        """
        pass

    @staticmethod
    def display_row_express(証明: 型定義クラス.証明クラス, 表現形: str) -> None:  # type: ignore
        """式を評価せずに表示する  
        要改修:
            ()が評価されて消えてしまう。  
            x/xは評価されて1になってしまう。（変数宣言する必要あり）  

        """
        pass

    @staticmethod
    def condition_logical_or(証明: 型定義クラス.証明クラス, コンディションず: tuple[型定義クラス.数理的コンディション, 型定義クラス.数理的コンディション]) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    @staticmethod
    def condition_logical_and(証明: 型定義クラス.証明クラス, コンディションず: tuple[型定義クラス.数理的コンディション, 型定義クラス.数理的コンディション]) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass


# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
