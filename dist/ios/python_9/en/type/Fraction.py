# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from collections.abc import Callable
from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import overload
from fractions import Fraction as NativeFraction


class Fraction:
    def __init__(self, proof: DefineType.Proof, express:  Union[str , express_fraction] ):
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
    def is_integer(self) ->  Union[bool , None] :  # type: ignore
        pass

    @property
    def numerator(self) -> int:  # type: ignore
        pass

    @property
    def denominator(self) -> int:  # type: ignore
        pass

    @property
    def number(self) ->  Union[int , DefineType.NativeFraction] :  # type: ignore
        pass

    def can_cast(self, type: type[DefineType.Float] | type[DefineType.Integer]) -> bool:  # type: ignore
        pass

    def get_coefficients(self, focus_variable: str, should_limit_integer: bool = False) -> list[Fraction]:  # type: ignore
        pass

    def __eq__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Equation] :  # type: ignore
        pass

    def __ne__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Unequation] :  # type: ignore
        pass

    def __lt__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __le__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __gt__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __ge__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def display(self):
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[DefineType.Float]) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Formula]) -> DefineType.Formula:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Integer]) -> DefineType.Integer:  # type: ignore
        ...

    def __rshift__(self, type: type[DefineType.Float] | type[DefineType.Formula] | type[DefineType.Integer]) ->  Union[DefineType.Formula , DefineType.Float , DefineType.Integer] :  # type: ignore
        pass

    @overload
    def __add__(self, formula:  Union[DefineType.Integer , int , Fraction] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __add__(self, formula:   Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __add__(self, formula:   DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __add__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction | DefineType.Formula) -> DefineType.Formula |  Union[Fraction , DefineType.Integer]  | DefineType.Float:  # type: ignore
        pass

    @overload
    def __sub__(self, formula:  Union[DefineType.Integer , int , Fraction] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __sub__(self, formula:   Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __sub__(self, formula:   DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __sub__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction | DefineType.Formula) -> DefineType.Formula |  Union[Fraction , DefineType.Integer]  | DefineType.Float:  # type: ignore
        pass

    def __neg__(self) -> Fraction:  # type: ignore
        pass

    @overload
    def __mul__(self, formula:  Union[DefineType.Integer , int , Fraction] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __mul__(self, formula:   Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __mul__(self, formula:  DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mul__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction | DefineType.Formula) -> DefineType.Formula |  Union[Fraction , DefineType.Integer]  | DefineType.Float:  # type: ignore
        pass

    @overload
    def __truediv__(self, formula:  Union[DefineType.Integer , int , Fraction] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __truediv__(self, formula:   Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __truediv__(self, formula:   DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __truediv__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction | DefineType.Formula) -> DefineType.Formula |  Union[Fraction , DefineType.Integer]  | DefineType.Float:  # type: ignore
        pass

    @overload
    def __mod__(self, formula:  Union[DefineType.Integer , int , Fraction] ) ->  Union[DefineType.Integer , Fraction] :  # type: ignore
        ...

    @overload
    def __mod__(self, formula:  Union[float , DefineType.Float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __mod__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mod__(self, formula:  Union[DefineType.Formula , float , int , DefineType.Integer , DefineType.Float , Fraction] ) ->  Union[DefineType.Integer , DefineType.Float , Fraction , DefineType.Formula] :  # type: ignore
        """[%] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __floordiv__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction) -> DefineType.Integer:  # type: ignore
        ...

    @overload
    def __floordiv__(self, formula: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __floordiv__(self, formula:   Union[DefineType.Formula , float , int , DefineType.Integer , DefineType.Float , Fraction] ) ->  Union[DefineType.Formula , DefineType.Integer] :  # type: ignore
        """[//] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __pow__(self, formula: DefineType.Integer | int |  Union[DefineType.Float , float]  | Fraction | DefineType.Formula) -> DefineType.Formula:  # type: ignore
        pass

    @overload
    def __radd__(self, formula:  Union[int , DefineType.Integer] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __radd__(self, formula: float) -> DefineType.Float:  # type: ignore
        ...

    def __radd__(self, formula:  float |  Union[int , DefineType.Integer] ) -> DefineType.Float |  Union[Fraction , DefineType.Integer] :  # type: ignore
        pass

    @overload
    def __rsub__(self, formula:  Union[int , DefineType.Integer] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __rsub__(self, formula: float) -> DefineType.Float:  # type: ignore
        ...

    def __rsub__(self, formula:  float |  Union[int , DefineType.Integer] ) -> DefineType.Float |  Union[Fraction , DefineType.Integer] :  # type: ignore
        pass

    @overload
    def __rmul__(self, formula:  Union[int , DefineType.Integer] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __rmul__(self, formula: float) -> DefineType.Float:  # type: ignore
        ...

    def __rmul__(self, formula:  float |  Union[int , DefineType.Integer] ) -> DefineType.Float |  Union[Fraction , DefineType.Integer] :  # type: ignore
        pass

    @overload
    def __rtruediv__(self, formula:  Union[int , DefineType.Integer] ) ->  Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __rtruediv__(self, formula: float) -> DefineType.Float:  # type: ignore
        ...

    def __rtruediv__(self, formula:  float |  Union[int , DefineType.Integer] ) -> DefineType.Float |  Union[Fraction , DefineType.Integer] :  # type: ignore
        pass

    @overload
    def __rmod__(self, formula:  Union[int , DefineType.Integer] ) ->  Union[DefineType.Integer , Fraction] :  # type: ignore
        ...

    @overload
    def __rmod__(self, formula: float) -> DefineType.Float:  # type: ignore
        ...

    def __rmod__(self, formula: float |  Union[int , DefineType.Integer] ) ->  Union[DefineType.Integer , DefineType.Float , Fraction] :  # type: ignore
        """[%] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rfloordiv__(self, formula:    Union[float , int] ) -> DefineType.Integer:  # type: ignore
        """[//] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rpow__(self, formula:  Union[int , DefineType.Integer] ) -> DefineType. Union[Fraction , DefineType.Integer] :  # type: ignore
        ...

    @overload
    def __rpow__(self, formula: float) -> DefineType.Formula:  # type: ignore
        ...

    def __rpow__(self, formula:  Union[int , DefineType.Integer]  | float) -> DefineType. Union[Fraction , DefineType.Integer]  | DefineType.Formula:  # type: ignore
        pass






# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import DefineType
    express_fraction = tuple[ Union[int , float , DefineType.NativeFraction] ,
                              Union[int , float , DefineType.NativeFraction] ]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
