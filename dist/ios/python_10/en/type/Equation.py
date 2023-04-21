# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
# from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal
import re
from typing import overload
from typing import TYPE_CHECKING


class Equation:
    def __init__(self, proof: DefineType.Proof, equation: str | term_pair):
        pass



    # @abstractmethod
    def text(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> DefineType.symbol_condition:  # type: ignore
        """sum

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: sum result

        Examples:
            >>> print(testfunc(2,5))
            7
        """
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

    def __lshift__(self, other: DefineType.SymbolCondition) -> DefineType.MathConditional:  # type: ignore
        pass

    def can_cast(self, type: DefineType.type_from_term_inequation) -> DefineType.SymbolicBool:  # type: ignore
        pass

    def make_figure(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> DefineType.Figure:  # type: ignore
        pass

    def plot(self, plot_ranges: DefineType.plotRange | DefineType.plotRanges | DefineType.plotRange_2d | None, alphabetic_axis_order: bool = True, title: str = '') -> DefineType.SymbolCondition:  # type: ignore
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
    def degree(self) -> int:  # type: ignore
        """式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        """式の変数
        """
        pass

    @property
    def evaluated(self) -> Equation | DefineType.SymbolicBool:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    def solve_diophantine_equation_d1_v2(self, parameter_symbol: str = 'k_', search_range: tuple[int, int] = (-5, 5), section_title: str = '１次２変数の不定方程式の解', section_id: str = 'solve_diophantine_equation_d1_v2') -> DefineType.VectorEquation:  # type: ignore
        pass

    def solve_diophantine_equation_d1_v2_disassembly_type(self, section_title: str = '１次２変数の不定方程式(分解型)の解', section_id: str = 'solve_diophantine_equation_d1_v2_disassembly_type') -> DefineType.VectorSolutions:  # type: ignore
        pass

    def solve_diophantine_equation_d2_v2_disassembly_type(self, is_natural_number: bool = False, section_title: str = '２次２変数の不定方程式(分解型)の解', section_id: str = 'solve_diophantine_equation_d2_v2_disassembly_type') -> DefineType.VectorSolutions:  # type: ignore
        pass

    def solve_diophantine_equation_Add_and_subtract_products(self, equation: DefineType.add_and_subtract_products_equation,  is_natural_number: bool = False, section_title: str = '２乗差の不定方程式の解', section_id: str = 'solve_diophantine_equation_Add_and_subtract_products') -> DefineType.VectorSolutions:  # type: ignore
        pass

    def solve_diophantine_equation_symmetric(self, variable_size_order: list[str] = [], is_order_strict: bool = False, section_title: str = '対称式の不定方程式の解', section_id: str = 'solve_diophantine_equation_symmetric') -> DefineType.VectorSolutions | None:  # type: ignore
        """対称不定方程式を解く

        注意
        ----------
        変数の大小関係の引数に柔軟に対応する拡張が必要かも。現実装は、対応範囲が狭い。
        解が自然数に限る

        Parameters
        ----------
        proof
        equation
            解くべき自然数不定方程式。右辺が整数である必要がある。
        variable_size_order:  
            変数の大小関係
        is_order_strict
            大小関係が厳密か、等号を含むか

        Returns
        -------
        solutions: 
            不定方程式の解のセット
        """
        pass

    def solve_equation_of_rapidly_increase_each_sides_difference(self, scan_range: tuple[int, int] = (0, 10), section_title: str = '急速に差が開く等式の解法', section_id: str = 'solve_equation_of_rapidly_increase_each_sides_difference'):
        pass

    def substitute(self, conditions: dict_float | dict_int | dict_term | Equation | DefineType.Equations, side: literal_direction | None = None) -> Equation:  # type: ignore
        pass

    def get_solution_range_of_diophantine_equation(self, variable_size_order: list[str], is_order_strict: bool = False,  section_title: str = '不定方程式の解の範囲', section_id: str = 'get_solution_range_of_diophantine_equation') -> list[DefineType.Inequation]:  # type: ignore
        pass

    def is_definition(self) -> bool:  # type: ignore
        pass

    def display(self, is_raw: bool = True):
        pass

    def solve(self, focus_variable: str) -> list[DefineType.Formula]:  # type: ignore
        pass

    def is_identity(self) -> bool:  # type: ignore
        pass

    def factorize(self) -> Equation:  # type: ignore
        pass

    def get_particular_solution_d1_v2(self, search_range: tuple[int, int]) -> dict_int | None:  # type: ignore
        pass

    def __add__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[+] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __sub__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[-] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __neg__(self) -> DefineType.Fraction:  # type: ignore
        pass

    def __mul__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[*] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __truediv__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[/] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __pow__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[**] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __radd__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[+] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rsub__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[-] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rmul__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[*] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rtruediv__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[/] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __rpow__(self, equation_or_term: DefineType.Equation | DefineType.Term | int | float | DefineType.NativeFraction) -> DefineType.Equation:  # type: ignore
        """[**] の中置演算子 

        引数:
            formula: 式
        結果: 
            Formula
        """
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
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
    def __rshift__(self, type: type[DefineEquation]) -> DefineEquation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[ExplainEquation]) -> ExplainEquation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Equation]) -> DefineType.Equation:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Unequation]) -> DefineType.Unequation:  # type: ignore
        ...

    def __rshift__(self, type: DefineType.type_from_term_inequation | ExplainEquation | DefineEquation) -> DefineType.symbol_condition | ExplainEquation | DefineEquation:  # type: ignore
        pass

    def castable_type(self) -> list[DefineType.type_from_term_inequation]:  # type: ignore
        pass

class Equation_2d(Equation):
    def __init__(self, proof: DefineType.Proof, equation: str | term_pair, main_variable: str = ''):
        pass


    @property
    def vietas_formulas_product(self) -> DefineType.Formula:  # type: ignore
        pass

    @property
    def vietas_formulas_addition(self) -> DefineType.Formula:  # type: ignore
        pass

    @property
    def discriminant(self) -> DefineType.Formula:  # type: ignore
        pass

    @property
    def a(self) -> DefineType.Formula:  # type: ignore
        pass

    @property
    def b(self) -> DefineType.Formula:  # type: ignore
        pass

    @property
    def c(self) -> DefineType.Formula:  # type: ignore
        pass

class ExplainEquation(Equation):
    def __init__(self, proof: DefineType.Proof, equation: str | formula_term_pair):
        pass
        # assert self.formulas[0].text in list(self._proof.variables.keys())


class DefineEquation(ExplainEquation):
    def __init__(self, proof: DefineType.Proof, equation: str | formula_term_pair):
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
    term_pair = tuple[DefineType.term, DefineType.term]
    formula_term_pair = tuple[DefineType.Formula, DefineType.term]
    dict_float = dict[str, float]
    dict_int = dict[str, int]
    dict_term = dict[str, DefineType.Term]
    literal_direction = Literal['left', 'right']
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
