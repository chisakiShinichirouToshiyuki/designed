# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import overload
from typing import TYPE_CHECKING


class SymbolicBool:
    def __init__(self, proof: DefineType.Proof, bool: bool):
        pass


    # @abstractmethod
    def variables(self) -> set[str]:  # type: ignore
        pass

    def display(self):
        pass



    # @abstractmethod
    def text(self) -> str:  # type: ignore
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

    def can_cast(self, type: DefineType.type_from_term_inequation) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def make_figure(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> DefineType.Figure:  # type: ignore
        pass

    def plot(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> DefineType.SymbolCondition:  # type: ignore
        pass


    @property
    def native_bool(self) -> bool:  # type: ignore
        pass

    def __bool__(self) -> bool:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> SymbolicBool:  # type: ignore
        pass

    def __eq__(self, other: bool | DefineType.symbol_condition) -> SymbolicBool:  # type: ignore
        pass

    def __ne__(self, other: bool | DefineType.symbol_condition) -> SymbolicBool:  # type: ignore
        pass

    @overload
    def __and__(self, other: bool | SymbolicBool) -> SymbolicBool:  # type: ignore
        ...

    @overload
    def __and__(self, other: DefineType.symbol_range) -> DefineType.symbol_condition:  # type: ignore
        ...

    def __and__(self, other: bool | SymbolicBool | DefineType.symbol_range) -> DefineType.symbol_condition:  # type: ignore
        pass

    @overload
    def __or__(self, other: bool | SymbolicBool) -> SymbolicBool:  # type: ignore
        ...

    @overload
    def __or__(self, other: DefineType.symbol_range) -> DefineType.symbol_condition:  # type: ignore
        ...

    def __or__(self, other: bool | SymbolicBool | DefineType.symbol_range) -> DefineType.symbol_condition:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[SymbolicBool]) -> SymbolicBool:  # type: ignore
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
    def __rshift__(self, type: type[DefineType.DefineEquation]) -> DefineType.DefineEquation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.ExplainEquation]) -> DefineType.ExplainEquation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Unequation]) -> DefineType.Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation | DefineType.ExplainEquation | DefineType.DefineEquation) -> DefineType.symbol_condition | DefineType.ExplainEquation | DefineType.DefineEquation:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
