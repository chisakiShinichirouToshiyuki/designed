# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import overload
from typing import TYPE_CHECKING
import math
from IPython.display import Markdown  # type: ignore


class ComplexCondition:
    def __init__(self, proof: DefineType.Proof, express: str):
        pass



    # @abstractmethod
    def variables(self) -> set[str]:  # type: ignore
        pass


    # @abstractmethod
    def text(self) -> str:  # type: ignore
        pass

    @property
    def logical_tree(self) -> DefineType.MarkdownContents:  # type: ignore
        pass

    def __invert__(self) -> DefineType.symbol_condition:  # type: ignore
        pass

    def __and__(self, other: bool | DefineType.symbol_condition) -> DefineType.symbol_condition:  # type: ignore
        """ 論理和の中置演算子

        Args:
            other : 演算対象

        """
        pass

    def __or__(self, other: bool | DefineType.symbol_condition) -> DefineType.symbol_condition:  # type: ignore
        pass

    def __eq__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __ne__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __lt__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __le__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __gt__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __ge__(self, other: bool | DefineType.symbol_condition) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __lshift__(self, other: DefineType.SymbolCondition) -> DefineType.MathConditional:  # type: ignore
        pass

    def display(self):
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
    def __rshift__(self, type: type[ComplexCondition_v1]) -> ComplexCondition_v1:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[ComplexCondition_v2]) -> ComplexCondition_v2:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition]) -> DefineType.ComplexCondition:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Unequation]) -> DefineType.Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation) -> DefineType.symbol_condition:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass

    def display_logical_tree(self) -> ComplexCondition:  # type: ignore
        pass

    def make_figure(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> DefineType.Figure:  # type: ignore
        pass

    def plot(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> ComplexCondition:  # type: ignore
        pass

    def can_cast(self, type: DefineType.type_from_term_inequation) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

class ComplexCondition_v1(ComplexCondition):
    def __init__(self, proof: DefineType.Proof, express: str):
        pass


    # Getter
    @property
    def range(self) -> DefineType.markdown_str:  # type: ignore
        pass

    def can_get_set_integer(self, set_limit: int = 1000, should_raise_error: bool = False) -> bool:  # type: ignore
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
    def __rshift__(self, type: type[ComplexCondition_v1]) -> ComplexCondition_v1:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[ComplexCondition_v2]) -> ComplexCondition_v2:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition]) -> DefineType.ComplexCondition:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Unequation]) -> DefineType.Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation) -> DefineType.symbol_condition:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass

    def display_range(self):
        pass

    def get_set_integer(self, set_limit: int = 1000) -> set[int]:  # type: ignore
        pass

    def __sub__(self, formula: ComplexCondition_v1) -> ComplexCondition_v1 | DefineType.Equation:  # type: ignore
        pass

class ComplexCondition_v2(ComplexCondition):
    def __init__(self, proof: DefineType.Proof,  express: str):
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
    def __rshift__(self, type: type[ComplexCondition_v1]) -> ComplexCondition_v1:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[ComplexCondition_v2]) -> ComplexCondition_v2:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ComplexCondition]) -> DefineType.ComplexCondition:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Unequation]) -> DefineType.Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation) -> DefineType.symbol_condition:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
