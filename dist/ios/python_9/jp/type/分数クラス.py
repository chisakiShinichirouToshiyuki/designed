# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from collections.abc import Callable
from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import overload
from fractions import Fraction as NativeFraction


class 分数クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形:  Union[str , express_fraction] ):
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
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def 抽象木(self) -> 抽象木クラス.抽象木クラス:  # type: ignore
        pass

    @property
    def 整数かい(self) ->  Union[bool , None] :  # type: ignore
        pass

    @property
    def 分子(self) -> int:  # type: ignore
        pass

    @property
    def 分母(self) -> int:  # type: ignore
        pass

    @property
    def number(self) ->  Union[int , 型定義クラス.NativeFraction] :  # type: ignore
        pass

    def 変換できるか(self, type: type[型定義クラス.有限小数クラス] | type[型定義クラス.整数クラス]) -> bool:  # type: ignore
        pass

    def 取得する_係数ず(self, ターゲット変数: str, 制限するか_整数の範囲: bool = False) -> list[分数クラス]:  # type: ignore
        pass

    def __eq__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.方程式クラス] :  # type: ignore
        pass

    def __ne__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.非等式クラス] :  # type: ignore
        pass

    def __lt__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __le__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __gt__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __ge__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def 表示する(self):
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.有限小数クラス]) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.式クラス]) -> 型定義クラス.式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.整数クラス]) -> 型定義クラス.整数クラス:  # type: ignore
        ...

    def __rshift__(self, type: type[型定義クラス.有限小数クラス] | type[型定義クラス.式クラス] | type[型定義クラス.整数クラス]) ->  Union[型定義クラス.式クラス , 型定義クラス.有限小数クラス , 型定義クラス.整数クラス] :  # type: ignore
        pass

    @overload
    def __add__(self, 式:  Union[型定義クラス.整数クラス , int , 分数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __add__(self, 式:   Union[型定義クラス.有限小数クラス , float] ) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __add__(self, 式:   型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __add__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス | 型定義クラス.式クラス) -> 型定義クラス.式クラス |  Union[分数クラス , 型定義クラス.整数クラス]  | 型定義クラス.有限小数クラス:  # type: ignore
        pass

    @overload
    def __sub__(self, 式:  Union[型定義クラス.整数クラス , int , 分数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __sub__(self, 式:   Union[型定義クラス.有限小数クラス , float] ) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __sub__(self, 式:   型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __sub__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス | 型定義クラス.式クラス) -> 型定義クラス.式クラス |  Union[分数クラス , 型定義クラス.整数クラス]  | 型定義クラス.有限小数クラス:  # type: ignore
        pass

    def __neg__(self) -> 分数クラス:  # type: ignore
        pass

    @overload
    def __mul__(self, 式:  Union[型定義クラス.整数クラス , int , 分数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __mul__(self, 式:   Union[型定義クラス.有限小数クラス , float] ) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __mul__(self, 式:  型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __mul__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス | 型定義クラス.式クラス) -> 型定義クラス.式クラス |  Union[分数クラス , 型定義クラス.整数クラス]  | 型定義クラス.有限小数クラス:  # type: ignore
        pass

    @overload
    def __truediv__(self, 式:  Union[型定義クラス.整数クラス , int , 分数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __truediv__(self, 式:   Union[型定義クラス.有限小数クラス , float] ) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __truediv__(self, 式:   型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __truediv__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス | 型定義クラス.式クラス) -> 型定義クラス.式クラス |  Union[分数クラス , 型定義クラス.整数クラス]  | 型定義クラス.有限小数クラス:  # type: ignore
        pass

    @overload
    def __mod__(self, 式:  Union[型定義クラス.整数クラス , int , 分数クラス] ) ->  Union[型定義クラス.整数クラス , 分数クラス] :  # type: ignore
        ...

    @overload
    def __mod__(self, 式:  Union[float , 型定義クラス.有限小数クラス] ) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __mod__(self, 式: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __mod__(self, 式:  Union[型定義クラス.式クラス , float , int , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス , 分数クラス] ) ->  Union[型定義クラス.整数クラス , 型定義クラス.有限小数クラス , 分数クラス , 型定義クラス.式クラス] :  # type: ignore
        """[%] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __floordiv__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス) -> 型定義クラス.整数クラス:  # type: ignore
        ...

    @overload
    def __floordiv__(self, 式: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __floordiv__(self, 式:   Union[型定義クラス.式クラス , float , int , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス , 分数クラス] ) ->  Union[型定義クラス.式クラス , 型定義クラス.整数クラス] :  # type: ignore
        """[//] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __pow__(self, 式: 型定義クラス.整数クラス | int |  Union[型定義クラス.有限小数クラス , float]  | 分数クラス | 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @overload
    def __radd__(self, 式:  Union[int , 型定義クラス.整数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __radd__(self, 式: float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __radd__(self, 式:  float |  Union[int , 型定義クラス.整数クラス] ) -> 型定義クラス.有限小数クラス |  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        pass

    @overload
    def __rsub__(self, 式:  Union[int , 型定義クラス.整数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __rsub__(self, 式: float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rsub__(self, 式:  float |  Union[int , 型定義クラス.整数クラス] ) -> 型定義クラス.有限小数クラス |  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        pass

    @overload
    def __rmul__(self, 式:  Union[int , 型定義クラス.整数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __rmul__(self, 式: float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rmul__(self, 式:  float |  Union[int , 型定義クラス.整数クラス] ) -> 型定義クラス.有限小数クラス |  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        pass

    @overload
    def __rtruediv__(self, 式:  Union[int , 型定義クラス.整数クラス] ) ->  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __rtruediv__(self, 式: float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rtruediv__(self, 式:  float |  Union[int , 型定義クラス.整数クラス] ) -> 型定義クラス.有限小数クラス |  Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        pass

    @overload
    def __rmod__(self, 式:  Union[int , 型定義クラス.整数クラス] ) ->  Union[型定義クラス.整数クラス , 分数クラス] :  # type: ignore
        ...

    @overload
    def __rmod__(self, 式: float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rmod__(self, 式: float |  Union[int , 型定義クラス.整数クラス] ) ->  Union[型定義クラス.整数クラス , 型定義クラス.有限小数クラス , 分数クラス] :  # type: ignore
        """[%] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __rfloordiv__(self, 式:    Union[float , int] ) -> 型定義クラス.整数クラス:  # type: ignore
        """[//] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rpow__(self, 式:  Union[int , 型定義クラス.整数クラス] ) -> 型定義クラス. Union[分数クラス , 型定義クラス.整数クラス] :  # type: ignore
        ...

    @overload
    def __rpow__(self, 式: float) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __rpow__(self, 式:  Union[int , 型定義クラス.整数クラス]  | float) -> 型定義クラス. Union[分数クラス , 型定義クラス.整数クラス]  | 型定義クラス.式クラス:  # type: ignore
        pass






# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import 型定義クラス
    express_fraction = tuple[ Union[int , float , 型定義クラス.NativeFraction] ,
                              Union[int , float , 型定義クラス.NativeFraction] ]
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
