# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import TYPE_CHECKING
from typing import Literal
from typing import overload
import re


class Unequation:
    def __init__(self, proof: DefineType.Proof, equation:  Union[str , express_term] ):
        pass



    # @abstractmethod
    def text(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> DefineType.symbol_condition:  # type: ignore
        pass

    def __and__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.symbol_condition:  # type: ignore
        """ 論理和の中置演算子

        Args:
            other : 演算対象

        """
        pass

    def __or__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.symbol_condition:  # type: ignore
        pass

    def __eq__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __ne__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __lt__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __le__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __gt__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __ge__(self, other:  Union[bool , DefineType.symbol_condition] ) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __lshift__(self, other: DefineType.SymbolCondition) -> DefineType.MathConditional:  # type: ignore
        pass

    def can_cast(self, type: DefineType.type_from_term_inequation) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def make_figure(self, plot_ranges:  Union[DefineType.plotRange , DefineType.plotRanges , DefineType.plotRange_2d , None] , alphabetic_axis_order: bool = True, title: str = '') -> DefineType.Figure:  # type: ignore
        pass

    def plot(self, plot_ranges:  Union[DefineType.plotRange , DefineType.plotRanges , DefineType.plotRange_2d , None] , alphabetic_axis_order: bool = True, title: str = '') -> DefineType.SymbolCondition:  # type: ignore
        pass


    @property
    def formulas(self) -> tuple[DefineType.Formula, DefineType.Formula]:  # type: ignore
        pass

    @property
    def text_forDisplay(self) -> str:  # type: ignore
        pass

    @property
    def text_for_input(self) -> str:  # type: ignore
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        """式の変数
        """
        pass

    @property
    def evaluated(self) ->  Union[Unequation , DefineType.SymbolicBool] :  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[DefineType.SymbolicBool]) -> DefineType.SymbolicBool:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Inequation_v1]) -> DefineType.Inequation_v1:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Inequation_v2]) -> DefineType.Inequation_v2:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Inequation]) -> DefineType.Inequation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition_v1]) -> DefineType.ComplexCondition_v1:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition_v2]) -> DefineType.ComplexCondition_v2:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition]) -> DefineType.ComplexCondition:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[Unequation]) -> Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation) -> DefineType.symbol_condition:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass

    def substitute(self, conditions: dict[str, float] | dict[str, int] | dict[str, DefineType.Term] |  Union[DefineType.Equation , DefineType.Equations] , side: Literal['left', 'right'] | None = None) -> Unequation:  # type: ignore
        pass

    def display(self, is_raw: bool = True):
        pass

    def is_identity(self) -> bool:  # type: ignore
        pass

    def factorize(self) -> Unequation:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
    express_term = tuple[DefineType.term, DefineType.term]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
