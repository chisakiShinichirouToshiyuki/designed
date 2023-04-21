# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from collections.abc import Callable
from IPython.display import Markdown, Math  # type: ignore
from typing import overload
from typing import TYPE_CHECKING


class Float:
    def __init__(self, proof: DefineType.Proof, express: float):
        pass


    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    @property
    def degree(self) -> int:  # type: ignore
        """式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        pass

    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def ast(self) -> Ast.Ast:  # type: ignore
        pass

    @property
    def is_integer(self) -> bool | None:  # type: ignore
        pass

    @property
    def number(self) -> float:  # type: ignore
        pass

    def can_cast(self, type: type[DefineType.Integer] | type[DefineType.Fraction]) -> bool:  # type: ignore
        pass

    def get_coefficients(self, focus_variable: str, should_limit_integer: bool = False) -> list[Float]:  # type: ignore
        pass

    def __eq__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Equation:  # type: ignore
        pass

    def __ne__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Unequation:  # type: ignore
        pass

    def __lt__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Inequation:  # type: ignore
        pass

    def __le__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Inequation:  # type: ignore
        pass

    def __gt__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Inequation:  # type: ignore
        pass

    def __ge__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Inequation:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def display(self):
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __add__(self, formula:  float | int | Float | DefineType.Integer | DefineType.Fraction) -> Float:  # type: ignore
        ...

    @overload
    def __add__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __add__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction | DefineType.Formula) -> Float | DefineType.Formula:  # type: ignore
        pass

    @overload
    def __sub__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction) -> Float:  # type: ignore
        ...

    @overload
    def __sub__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __sub__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction | DefineType.Formula) -> Float | DefineType.Formula:  # type: ignore
        pass

    def __neg__(self) -> Float:  # type: ignore
        pass

    @overload
    def __mul__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction) -> Float:  # type: ignore
        ...

    @overload
    def __mul__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mul__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction | DefineType.Formula) -> Float | DefineType.Formula:  # type: ignore
        pass

    @overload
    def __truediv__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction) -> Float:  # type: ignore
        ...

    @overload
    def __truediv__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __truediv__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction | DefineType.Formula) -> Float | DefineType.Formula:  # type: ignore
        pass

    @overload
    def __mod__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction) -> Float:  # type: ignore
        ...

    @overload
    def __mod__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mod__(self, formula: DefineType.Formula | float | int | DefineType.Integer | Float | DefineType.Fraction) -> Float | DefineType.Formula:  # type: ignore
        """[%] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __floordiv__(self, formula: DefineType.Integer | int | Float | float | DefineType.Fraction) -> DefineType.Integer:  # type: ignore
        ...

    @overload
    def __floordiv__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __floordiv__(self, formula:  DefineType.Formula | float | int | DefineType.Integer | Float | DefineType.Fraction) -> DefineType.Formula | DefineType.Integer:  # type: ignore
        """[//] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __pow__(self, formula: DefineType.Formula | float | int | DefineType.Fraction | DefineType.Integer | Float) -> DefineType.Formula:  # type: ignore
        """[**] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __radd__(self, formula: float | int) -> Float:  # type: ignore
        """[+] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rsub__(self, formula: float | int) -> Float:  # type: ignore
        """[-] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rmul__(self, formula: float | int) -> Float:  # type: ignore
        """[*] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rtruediv__(self, formula: float | int) -> Float:  # type: ignore
        """[/] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rpow__(self, formula: float | int) -> DefineType.Formula:  # type: ignore
        """[**] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rmod__(self, formula:  float | int) -> Float:  # type: ignore
        """[%] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rfloordiv__(self, formula:  float | int) -> DefineType.Integer:  # type: ignore
        """[//] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rshift__(self,  type: type[DefineType.Integer]) -> DefineType.Integer:  # type: ignore
        ...

    @overload
    def __rshift__(self,  type: type[DefineType.Formula]) -> DefineType.Formula:  # type: ignore
        ...

    @overload
    def __rshift__(self,  type: type[DefineType.Fraction]) -> DefineType.Fraction:  # type: ignore
        ...

    def __rshift__(self, type: type[DefineType.Integer] | type[DefineType.Formula] | type[DefineType.Fraction]) -> DefineType.Formula | DefineType.Integer | DefineType.Fraction:  # type: ignore
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
