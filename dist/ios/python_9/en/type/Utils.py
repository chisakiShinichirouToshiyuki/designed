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
    def display(contents:  Union[str , Markdown] ) -> None:  # type: ignore
        pass

    @staticmethod
    def getPrimes(range: tuple[int, int]) -> list[int]:  # type: ignore
        pass



    @staticmethod
    @overload
    def euclideanAlgorithm(proof: DefineType.Proof, terms: tuple[int, int], section_title: str) -> tuple[int, int]:  # type: ignore
        ...

    @staticmethod
    @overload
    def euclideanAlgorithm(proof: DefineType.Proof, terms: tuple[str, str], section_title: str) -> tuple[str, str]:  # type: ignore
        ...

    @staticmethod
    def euclideanAlgorithm(proof: DefineType.Proof, terms: tuple[str, str] | tuple[int, int], section_title: str = 'euclideanAlgorithm') -> tuple[int, int] | tuple[str, str]:  # type: ignore
        pass

    @staticmethod
    def cast(proof: DefineType.Proof, type: DefineType.term_type, text: str) ->  Union[DefineType.Integer , DefineType.Float , DefineType.Fraction , DefineType.Formula] :  # type: ignore
        pass

    @staticmethod
    def can_cast(type: DefineType.term_type, text: str) -> bool:  # type: ignore
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
    def display_row_express(proof: DefineType.Proof, express: str) -> None:  # type: ignore
        """式を評価せずに表示する  
        要改修:
            ()が評価されて消えてしまう。  
            x/xは評価されて1になってしまう。（変数宣言する必要あり）  

        """
        pass

    @staticmethod
    def condition_logical_or(proof: DefineType.Proof, conditions: tuple[DefineType.symbol_condition, DefineType.symbol_condition]) -> DefineType.symbol_condition:  # type: ignore
        pass

    @staticmethod
    def condition_logical_and(proof: DefineType.Proof, conditions: tuple[DefineType.symbol_condition, DefineType.symbol_condition]) -> DefineType.symbol_condition:  # type: ignore
        pass


# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
