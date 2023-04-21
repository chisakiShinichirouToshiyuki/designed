# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from collections.abc import Callable
from IPython.display import Markdown, Math  # type: ignore
from typing import cast
from typing import TYPE_CHECKING
from typing import Literal
import re
from typing import overload
from typing import Any


class 不等式クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: str | express_inequation, is_strict_mode: bool = False):
        pass



    # @abstractmethod
    def テキスト(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def __and__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的コンディション:  # type: ignore
        """ 論理和の中置演算子

        Args:
            相手 : 演算対象

        """
        pass

    def __or__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def __eq__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __ne__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __lt__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __le__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __gt__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __ge__(self, 相手: bool | 型定義クラス.数理的コンディション) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __lshift__(self, 相手: 型定義クラス.数理的条件クラス) -> 型定義クラス.数理的命題クラス:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def 作成する_図形(self, 範囲ず_プロット: 型定義クラス.プロット範囲 | 型定義クラス.プロット範囲ず | 型定義クラス.プロット範囲_2次 | None, アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.図形クラス:  # type: ignore
        pass

    def プロットする(self, 範囲ず_プロット: 型定義クラス.プロット範囲 | 型定義クラス.プロット範囲ず | 型定義クラス.プロット範囲_2次 | None, アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.数理的条件クラス:  # type: ignore
        pass


    @property
    def 式ず(self) -> tuple[型定義クラス.式クラス, 型定義クラス.式クラス]:  # type: ignore
        pass

    @property
    def テキスト_因数分解後(self) -> str:  # type: ignore
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    @property
    def 次数(self) -> int:  # type: ignore
        """式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        pass

    @property
    def solved(self) -> 不等式クラス | 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    @property
    def 評価済(self) -> 不等式クラス | 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.数理的真偽クラス]) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v1クラス]) -> 型定義クラス.複合条件_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v2クラス]) -> 型定義クラス.複合条件_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件クラス]) -> 型定義クラス.複合条件クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.方程式クラス]) -> 型定義クラス.方程式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.非等式クラス]) -> 型定義クラス.非等式クラス:  # type: ignore
        ...

    def __rshift__(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def 変換可能な型(self) -> list[型定義クラス.type_from_term_inequation]:  # type: ignore
        pass

    def 変換できるか(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def 因数分解する(self) -> 不等式クラス:  # type: ignore
        pass

    def 表示する(self, state: Literal['row', 'factorized', 'factorized_and_split'] = 'factorized_and_split'):
        pass

class 不等式_v1クラス(不等式クラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: str | express_inequation, is_strict_mode: bool = False):
        pass


    # Getter
    @property
    def range(self) -> 型定義クラス.markdown_str:  # type: ignore
        pass

    def 取得できるか_整数の集合(self, 走査範囲: int = 1000, エラーを出すべきか: bool = False) -> bool:  # type: ignore
        pass

    def __sub__(self, 式: 不等式_v1クラス) -> 型定義クラス.複合条件_v2クラス | 型定義クラス.複合条件_v1クラス | 型定義クラス.方程式クラス:  # type: ignore
        pass

    def __eq__(self, 式: 不等式_v1クラス) -> bool:  # type: ignore
        pass

    def __ne__(self, 式: 不等式_v1クラス) -> bool:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v1クラス]) -> 型定義クラス.複合条件_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v2クラス]) -> 型定義クラス.複合条件_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件クラス]) -> 型定義クラス.複合条件クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.方程式クラス]) -> 型定義クラス.方程式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式クラス]) -> 型定義クラス.不等式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.数理的真偽クラス]) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.非等式クラス]) -> 型定義クラス.非等式クラス:  # type: ignore
        ...

    def __rshift__(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def 変換可能な型(self) -> list[型定義クラス.type_from_term_inequation]:  # type: ignore
        pass

    def 取得する_整数集合(self, 走査範囲: int = 1000) -> set[int]:  # type: ignore
        pass

class 不等式_v2クラス(不等式クラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: str | express_inequation, is_strict_mode: bool = False):
        pass

    def __sub__(self, 式: 不等式_v1クラス) -> 型定義クラス.複合条件_v2クラス | 型定義クラス.方程式クラス:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.数理的真偽クラス]) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式クラス]) -> 型定義クラス.不等式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v1クラス]) -> 型定義クラス.複合条件_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v2クラス]) -> 型定義クラス.複合条件_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件クラス]) -> 型定義クラス.複合条件クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.方程式クラス]) -> 型定義クラス.方程式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.非等式クラス]) -> 型定義クラス.非等式クラス:  # type: ignore
        ...

    def __rshift__(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def 変換可能な型(self) -> list[型定義クラス.type_from_term_inequation]:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
    express_inequation = tuple[型定義クラス.項, 型定義クラス.項]
    literal_eq = Literal['=']
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
