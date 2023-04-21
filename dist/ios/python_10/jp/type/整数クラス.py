# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
# from typing import TYPE_CHECKING
from typing import Literal
import math
from typing import overload


class 整数クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: int):
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
    def 整数かい(self) -> bool | None:  # type: ignore
        pass

    @property
    def number(self) -> int:  # type: ignore
        pass

    @property
    def 素数かい(self) -> bool:  # type: ignore
        pass

    @property
    def 約数の個数(self) -> 整数クラス:  # type: ignore
        pass

    @property
    def 約数の総和(self) -> 整数クラス:  # type: ignore
        pass

    @property
    def 約数ず(self) -> list[int]:  # type: ignore
        pass

    @staticmethod
    def 証明する_無理数か(証明: 型定義クラス.証明クラス, root: str = 'm', 分子: str = 'q', 分母: str = 'l', 章タイトル: str = "無理数の証明") -> bool:  # type: ignore
        pass

    @staticmethod
    def 証明する_素数の無限性(証明: 型定義クラス.証明クラス, 章タイトル: str = '素数が無限にある証明', 章ID: str = '証明する_素数の無限性'):
        pass

    def 素因数分解する(self) -> dict[int, int]:  # type: ignore
        pass

    def 取得する_自身以下の素数ず(self) -> list[int]:  # type: ignore
        pass

    def 変換できるか(self, type: type[型定義クラス.有限小数クラス] | type[型定義クラス.分数クラス]) -> bool:  # type: ignore
        pass

    def 取得する_係数ず(self, ターゲット変数: str, 制限するか_整数の範囲: bool = False) -> list[整数クラス]:  # type: ignore
        pass

    @overload
    def 互いに素かい(self, 相手: 整数クラス | int, 互いに素なペア: list[tuple[int | 整数クラス | 型定義クラス.式クラス, int | 整数クラス | 型定義クラス.式クラス]] = []) -> bool:  # type: ignore
        ...

    @overload
    def 互いに素かい(self, 相手: 型定義クラス.式クラス, 互いに素なペア: list[tuple[int | 整数クラス | 型定義クラス.式クラス, int | 整数クラス | 型定義クラス.式クラス]] = []) -> bool | None:  # type: ignore
        ...

    def 互いに素かい(self, 相手: 整数クラス | int | 型定義クラス.式クラス, 互いに素なペア: list[tuple[int | 整数クラス | 型定義クラス.式クラス, int | 整数クラス | 型定義クラス.式クラス]] = []) -> bool | None:  # type: ignore
        pass

    def 取得する_積に分解したペア(self, uniqueness: Literal['combination', 'order'] = 'order', is_include_minus: bool = False) -> set[tuple[int, int]]:  # type: ignore
        pass

    def __eq__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.方程式クラス:  # type: ignore
        pass

    def __ne__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.非等式クラス:  # type: ignore
        pass

    def __lt__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.不等式クラス:  # type: ignore
        pass

    def __le__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.不等式クラス:  # type: ignore
        pass

    def __gt__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.不等式クラス:  # type: ignore
        pass

    def __ge__(self, 相手: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.不等式クラス:  # type: ignore
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
    def __rshift__(self, type: type[型定義クラス.分数クラス]) -> 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[整数クラス]) -> 整数クラス:  # type: ignore
        ...

    def __rshift__(self, type: type[型定義クラス.有限小数クラス] | type[型定義クラス.式クラス] | type[型定義クラス.分数クラス] | type[整数クラス]) -> 型定義クラス.式クラス | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス | 整数クラス:  # type: ignore
        pass

    @overload
    def __add__(self, 相手: 整数クラス | int) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __add__(self, 相手: 型定義クラス.分数クラス) -> 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __add__(self, 相手: 型定義クラス.有限小数クラス | float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __add__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __add__(self, 相手: 整数クラス | int | 型定義クラス.有限小数クラス | float | 型定義クラス.分数クラス | 型定義クラス.式クラス) -> 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.式クラス | 型定義クラス.分数クラス:  # type: ignore
        pass

    @overload
    def __sub__(self, 相手: 整数クラス | int) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __sub__(self, 相手: 型定義クラス.分数クラス) -> 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __sub__(self, 相手: 型定義クラス.有限小数クラス | float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __sub__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __sub__(self, 相手: 整数クラス | int | 型定義クラス.有限小数クラス | float | 型定義クラス.分数クラス | 型定義クラス.式クラス) -> 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.式クラス | 型定義クラス.分数クラス:  # type: ignore
        pass

    def __neg__(self) -> 整数クラス:  # type: ignore
        pass

    @overload
    def __mul__(self, 相手: 整数クラス | int) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __mul__(self, 相手: 型定義クラス.分数クラス) -> 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __mul__(self, 相手: 型定義クラス.有限小数クラス | float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __mul__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __mul__(self, 相手: 整数クラス | int | 型定義クラス.有限小数クラス | float | 型定義クラス.分数クラス | 型定義クラス.式クラス) -> 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.式クラス | 型定義クラス.分数クラス:  # type: ignore
        pass

    @overload
    def __truediv__(self, 相手: 整数クラス | int | 型定義クラス.分数クラス) -> 型定義クラス.分数クラス | 整数クラス:  # type: ignore
        ...

    @overload
    def __truediv__(self, 相手: 型定義クラス.有限小数クラス | float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __truediv__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __truediv__(self, 相手: 整数クラス | int | 型定義クラス.有限小数クラス | float | 型定義クラス.分数クラス | 型定義クラス.式クラス) -> 型定義クラス.有限小数クラス | 型定義クラス.式クラス | 型定義クラス.分数クラス | 整数クラス:  # type: ignore
        pass

    @overload
    def __mod__(self, 相手: 整数クラス | int) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __mod__(self, 相手: 型定義クラス.分数クラス) -> 整数クラス | 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __mod__(self, 相手: float | 型定義クラス.有限小数クラス) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __mod__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __mod__(self, 相手: 型定義クラス.式クラス | float | int | 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス) -> 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス | 型定義クラス.式クラス:  # type: ignore
        """[%] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __floordiv__(self, 相手: 整数クラス | int | 型定義クラス.有限小数クラス | float | 型定義クラス.分数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __floordiv__(self, 相手: 型定義クラス.式クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __floordiv__(self, 相手:  型定義クラス.式クラス | float | int | 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス) -> 型定義クラス.式クラス | 整数クラス:  # type: ignore
        """[//] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __pow__(self, 相手: 整数クラス | int) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __pow__(self, 相手: 型定義クラス.式クラス | float | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __pow__(self, 相手:  型定義クラス.式クラス | float | int | 整数クラス | 型定義クラス.有限小数クラス | 型定義クラス.分数クラス) -> 整数クラス | 型定義クラス.式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __radd__(self, 相手: int | 整数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __radd__(self, 相手:  float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __radd__(self, 相手: float | int | 整数クラス) -> 整数クラス | 型定義クラス.有限小数クラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rsub__(self, 相手: int | 整数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __rsub__(self, 相手:  float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rsub__(self, 相手: float | int | 整数クラス) -> 整数クラス | 型定義クラス.有限小数クラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rmul__(self, 相手: int | 整数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __rmul__(self, 相手:  float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rmul__(self, 相手: float | int | 整数クラス) -> 整数クラス | 型定義クラス.有限小数クラス:  # type: ignore
        """[*] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rtruediv__(self, 相手: int | 整数クラス) -> 整数クラス | 型定義クラス.分数クラス:  # type: ignore
        ...

    @overload
    def __rtruediv__(self, 相手:  float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rtruediv__(self, 相手: float | int | 整数クラス) -> 整数クラス | 型定義クラス.分数クラス | 型定義クラス.有限小数クラス:  # type: ignore
        """[/] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rpow__(self, 相手: int | 整数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __rpow__(self, 相手:  float) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def __rpow__(self, 相手: float | int | 整数クラス) -> 整数クラス | 型定義クラス.式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __rmod__(self, 相手: int | 整数クラス) -> 整数クラス:  # type: ignore
        ...

    @overload
    def __rmod__(self, 相手:  float) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    def __rmod__(self, 相手:  float | int | 整数クラス) -> 整数クラス | 型定義クラス.有限小数クラス:  # type: ignore
        """[%] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rfloordiv__(self, 相手:  float | int) -> 整数クラス:  # type: ignore
        """[//] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __eq__(self, 項: 型定義クラス.term_) -> 型定義クラス.数理的真偽クラス | 型定義クラス.方程式クラス:  # type: ignore
        pass

    def 取得する_乗数の剰余(self, power: int, mod: int, _範囲: tuple[int, int] = (1, 5)):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
