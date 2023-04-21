# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import overload
from typing import TYPE_CHECKING


class 数理的真偽クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, bool: bool):
        pass


    # @abstractmethod
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    def 表示する(self):
        pass



    # @abstractmethod
    def テキスト(self) -> str:  # type: ignore
        pass

    def __lt__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __le__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __gt__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __ge__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __lshift__(self, 相手: 型定義クラス.数理的条件クラス) -> 型定義クラス.数理的命題クラス:  # type: ignore
        pass

    def 変換できるか(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def 作成する_図形(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None] , アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.図形クラス:  # type: ignore
        pass

    def プロットする(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None] , アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.数理的条件クラス:  # type: ignore
        pass


    @property
    def 真偽(self) -> bool:  # type: ignore
        pass

    def __bool__(self) -> bool:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> 数理的真偽クラス:  # type: ignore
        pass

    def __eq__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 数理的真偽クラス:  # type: ignore
        pass

    def __ne__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 数理的真偽クラス:  # type: ignore
        pass

    @overload
    def __and__(self, 相手:  Union[bool , 数理的真偽クラス] ) -> 数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __and__(self, 相手: 型定義クラス.数理的範囲) -> 型定義クラス.数理的コンディション:  # type: ignore
        ...

    def __and__(self, 相手:  Union[bool , 数理的真偽クラス]  | 型定義クラス.数理的範囲) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    @overload
    def __or__(self, 相手:  Union[bool , 数理的真偽クラス] ) -> 数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __or__(self, 相手: 型定義クラス.数理的範囲) -> 型定義クラス.数理的コンディション:  # type: ignore
        ...

    def __or__(self, 相手:  Union[bool , 数理的真偽クラス]  | 型定義クラス.数理的範囲) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[数理的真偽クラス]) -> 数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式_v1クラス]) -> 型定義クラス.不等式_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式_v2クラス]) -> 型定義クラス.不等式_v2クラス:  # type: ignore
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
    def __rshift__(self, type: type[型定義クラス.定義式クラス]) -> 型定義クラス.定義式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.説明式クラス]) -> 型定義クラス.説明式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.方程式クラス]) -> 型定義クラス.方程式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.非等式クラス]) -> 型定義クラス.非等式クラス:  # type: ignore
        ...

    def __rshift__(self, type:  Union[型定義クラス.type_from_term_inequation , 型定義クラス.説明式クラス , 型定義クラス.定義式クラス] ) ->  Union[型定義クラス.数理的コンディション , 型定義クラス.説明式クラス , 型定義クラス.定義式クラス] :  # type: ignore
        pass

    def 変換可能な型(self) -> list[型定義クラス.type_from_term_inequation]:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
