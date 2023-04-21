# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
import random
from typing import overload
from typing import TYPE_CHECKING
from copy import deepcopy


default_condition: DefineType.condition = {
    'times': 0,
    'mod': [0]
}


class Formula:
    def __init__(self, proof: DefineType.Proof, text: str | float | int, variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}):
        pass


    @property
    def ast(self) -> Ast.Ast:  # type: ignore
        pass

    @property
    def completing_square(self) -> DefineType.squared_result:  # type: ignore
        pass

    @property
    def degree(self) -> int:  # type: ignore
        pass

    @property
    def factorized_elements(self) -> list[Formula]:  # type: ignore
        """因数分解の因数(次数なし)
        """
        pass

    @property
    def is_integer(self) -> bool | None:  # type: ignore
        pass

    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    def can_cast(self, type: type[DefineType.Integer] | type[DefineType.Float] | type[DefineType.Fraction]) -> bool:  # type: ignore
        pass

    def check_fo_symmetry(self) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def display(self):
        pass

    def differentiate(self, focus_variable: str) -> Formula:  # type: ignore
        pass

    def expand(self) -> Formula:  # type: ignore
        pass

    def factorize(self) -> Formula:  # type: ignore
        pass

    def fragile_substitute(self, subsitutee: tuple[str, Formula]) -> Formula:  # type: ignore
        pass

    def get_coefficients(self, focus_variable: str, should_limit_integer: bool = False) -> list[Formula]:  # type: ignore
        pass

    def get_factors(self) -> list[Formula]:  # type: ignore
        pass

    def identify_from_condition(self, divisor_quantity: int, range: tuple[int, int], section_title: str = '整数の特定', section_id: str = 'identify_from_condition') -> DefineType.Vector:  # type: ignore
        pass

    def integrate(self) -> Formula:  # type: ignore
        pass

    def is_integer_rough_check(self, rough_search: bool = False, only_positive: bool = True) -> bool | None:  # type: ignore
        pass

    def is_specific_times(self, times: int, expected_mod: list[int], condition: DefineType.condition = default_condition, section_title: str = 'proof_specific_times') -> bool:  # type: ignore
        pass

    def is_relatively_prime(self, other: DefineType.Integer | int | Formula, relational_prime_pairs: list[tuple[int | DefineType.Integer | Formula, int | DefineType.Integer | Formula]] = []) -> bool | None:  # type: ignore
        pass

    def make_figure(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None = None, title: str = '') -> DefineType.Figure:  # type: ignore
        pass

    def make_uni_variantization(self, target_variable: str):
        pass

    def rough_check_monotonically_increase(self, points: list[int] = list(range(1, 100, 20)), is_in_Natural: bool = True) -> bool | None:  # type: ignore
        pass

    def solve(self, focus_term: str = '') -> list[Formula]:  # type: ignore
        pass

    def substitute(self, conditions: DefineType.conditions_float | DefineType.conditions_int | DefineType.conditions_str | DefineType.conditions_term | DefineType.Equation | DefineType.Equations) -> Formula:  # type: ignore
        pass

    def proof_powers_modularity(self, mod: int, section_title: str = '乗数の剰余', section_id: str = 'proof_powers_modularity'):
        pass

    def plot(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None = None, title: str = '', color: DefineType.hsla = (220, 100, 50), label: str = '') -> Formula:  # type: ignore
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

    def __str__(self) -> str:  # type: ignore
        pass

    def __add__(self, other:  float | int | DefineType.Integer | DefineType.Float | DefineType.Fraction | Formula) -> Formula:  # type: ignore
        """[+] の中置演算子 

        引数:
            other: 演算子の左側の式
        結果: 
            Formula
        """
        pass

    def __sub__(self, other: Formula | float | int | DefineType.Fraction | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[-] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __neg__(self) -> Formula:  # type: ignore
        pass

    def __mul__(self, other: Formula | float | int | DefineType.Fraction | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[*] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __truediv__(self, other: Formula | float | int | DefineType.Fraction | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[/] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __pow__(self, other: Formula | float | int | DefineType.Fraction | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[**] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __mod__(self, other: Formula | float | int | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[%] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __floordiv__(self, other: Formula | float | int | DefineType.Integer | DefineType.Float) -> Formula:  # type: ignore
        """[//] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __radd__(self, other: float | int) -> Formula:  # type: ignore
        """[+] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rsub__(self, other: float | int) -> Formula:  # type: ignore
        """[-] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rmul__(self, other: float | int) -> Formula:  # type: ignore
        """[*] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rtruediv__(self, other: float | int) -> Formula:  # type: ignore
        """[/] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rpow__(self, other: float | int) -> Formula:  # type: ignore
        """[**] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rmod__(self, other:  float | int) -> Formula:  # type: ignore
        """[%] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rfloordiv__(self, other:  float | int) -> Formula:  # type: ignore
        """[//] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __eq__(self, other: str) -> str:  # type: ignore
        ...

    @overload
    def __eq__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Equation:  # type: ignore
        ...

    def __eq__(self, other: DefineType.term_ | str) -> DefineType.SymbolicBool | DefineType.Equation | str:  # type: ignore
        pass

    @overload
    def __ne__(self, other: str) -> str:  # type: ignore
        ...

    @overload
    def __ne__(self, other: DefineType.term_) -> DefineType.SymbolicBool | DefineType.Unequation:  # type: ignore
        ...

    def __ne__(self, other: DefineType.term_ | str) -> DefineType.SymbolicBool | DefineType.Unequation | str:  # type: ignore
        pass

    def check_operator(self, check_operator: list[DefineType.symbol_type]) -> DefineType.SymbolicBool:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[DefineType.Integer]) -> DefineType.Integer:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Float]) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Fraction]) -> DefineType.Fraction:  # type: ignore
        ...

    def __rshift__(self, type: type[DefineType.Integer] | type[DefineType.Float] | type[DefineType.Fraction]) -> DefineType.Float | DefineType.Integer | DefineType.Fraction:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
