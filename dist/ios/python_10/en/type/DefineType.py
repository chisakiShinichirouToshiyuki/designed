# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import Any
from typing import Literal
from typing import TYPE_CHECKING
from typing import TypedDict
from fractions import Fraction as NativeFraction
from .Proof import Proof
from .Ax import Ax
from .Figure import Figure
from .Range import Range
from .Equation import DefineEquation
from .Equation import ExplainEquation
from .Equations import Equations
from .Equations import VectorEquation
from .Equations import Solutions

from .Section import Section
from .MarkdownContents import MarkdownContents
from .RelationContent import RelationContent
from .SymbolicBool import SymbolicBool
from .MathConditional import MathConditional
from .MathConditional import MathConditional
# from Term import Term
from .Ast import Ast
from .Set import Set
from .Integer import Integer
from .Float import Float
from .Fraction import Fraction
from .Formula import Formula
from .Vector import Vector
from .Vector import IntegerPair
from .Vector import NaturalPair
from .Equation import Equation
from .Unequation import Unequation
from .VectorSolutions import VectorSolutions
from .Inequation import Inequation
from .Inequation import Inequation_v1
from .Inequation import Inequation_v2
from .ComplexCondition import ComplexCondition
from .ComplexCondition import ComplexCondition_v1
from .ComplexCondition import ComplexCondition_v2
from .FigureReservation import FigureReservation
from .VenDiagramReservation import VenDiagramReservation
from .Table import Table

DefineEquation = DefineEquation
ExplainEquation = ExplainEquation
Equations = Equations
Figure = Figure
Ax = Ax
Ast = Ast
Set = Set
Range = Range
SymbolCondition = Equation | Inequation | Unequation | ComplexCondition | SymbolicBool
Term = Formula | Float | Integer | Fraction


# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import _ad as AdapterTypes


class subtract_prime_result(TypedDict):
    term: Formula
    signInteger: Literal[1, -1]


class Modee(TypedDict):
    residual: int
    power: int


# Independent type
markdown_str = str
integer_candidate = Integer | Formula
integer_candidate_input = int | integer_candidate
integer_pair_input = tuple[integer_candidate_input, integer_candidate_input]
integer_pair = tuple[integer_candidate, integer_candidate]
condition_symbol = Literal['True', 'False']
number_symbol = Literal['oo', '-oo']
equation_symbol_ = Literal['=']
hsla = tuple[float | int, float | int, float | int, float |
             int] | tuple[float | int, float | int, float | int]
inequality_relation = Literal['<', '<=', '>', '>=']
inequation_symbol = Literal['<', '<=', '>', '>=']
term_type = type[Integer] | type[Float] | type[Fraction] | type[Formula]
table_data = dict[str, list[str | int | float]]
unequation_symbol = Literal['!=']
variable_symbol = Any
plotRange_ = tuple[tuple[int | float, int | float],
                   tuple[int | float, int | float]]
# Dependent type
symbol_relation_type = Literal[AdapterTypes.operator_symbol, number_symbol,
                               condition_symbol, equation_symbol_, inequation_symbol, unequation_symbol]
symbol_type = Literal[symbol_relation_type, 'symbol', condition_symbol]
type_from_term_inequation = \
    type[SymbolicBool] | type[Inequation] | type[Inequation_v1] | type[Inequation_v2] | type[Equation] | type[
        Unequation] | type[ComplexCondition] | type[ComplexCondition_v1] | type[ComplexCondition_v2]
variables = dict[str, variable_symbol]
single_condition = Equation | Unequation | Inequation | Inequation_v1 | Inequation_v2 | SymbolicBool
symbol_range = Equation | Unequation | Inequation | Inequation_v1 | Inequation_v2 | ComplexCondition | ComplexCondition_v1 | ComplexCondition_v2
symbol_condition = symbol_range | SymbolicBool

# Independent type


class squared_result(TypedDict):
    square: Formula
    correction_term: Formula


class add_and_subtract_products_equation(TypedDict):
    left_plus_term: Formula
    left_minus_term: Formula
    right_constant_term: Integer | Fraction


class euclidean_output_each_process(TypedDict):
    result: NaturalPair
    explain: Section


class euclidean_output(TypedDict):
    result: NaturalPair | integer_candidate
    explain: Section


class variable_type_optional(TypedDict, total=False):
    commutative: Literal[True]
    complex: Literal[True]
    composite: Literal[True]
    even: Literal[True]
    extended_negative: Literal[True]
    extended_nonnegative: Literal[True]
    extended_nonpositive: Literal[True]
    extended_nonzero: Literal[True]
    extended_positive: Literal[True]
    extended_real: Literal[True]
    finite: Literal[True]
    imaginary: Literal[True]
    infinite: Literal[True]
    integer: Literal[True]
    irrational: Literal[True]
    negative: Literal[True]
    noninteger: Literal[True]
    nonnegative: Literal[True]
    nonpositive: Literal[True]
    nonzero: Literal[True]
    odd: Literal[True]
    positive: Literal[True]
    prime: Literal[True]
    rational: Literal[True]
    real: Literal[True]
    zero: Literal[True]


class equation(TypedDict):
    formula_left: str
    formula_right: str


class vennData(TypedDict):
    label: str
    set: set[int] | set[str]
# Dependent type


variable_types_optional = dict[str, variable_type_optional]
explain = Section | RelationContent | str | MarkdownContents | Table | FigureReservation | VenDiagramReservation


class common_initialize_result(TypedDict):
    proof: Proof
    ast: AdapterTypes.astElement
    variables: set[str]


class equation_symbol(TypedDict):
    formula_left: variable_symbol
    formula_right: variable_symbol


class checked_variable(TypedDict):
    existed_variables: variables
    added_variables: set[str]


class condition(TypedDict):
    times: int
    mod: list[int]


term_instance = float | int | Integer | Float | Fraction | Formula
conditions_float = dict[str, float]
conditions_int = dict[str, int]
conditions_str = dict[str, str]
conditions_term = dict[str, Term]
conditions_fraction = dict[str, NativeFraction]
conditions_native = conditions_float | conditions_int | conditions_str
term_ = Term | float | int | NativeFraction
term = Term | str | float | int | NativeFraction
hex_rgb = tuple[int, int, int]
plot_color = Literal[
    'black',
    'red',
    'green',
    'orange'
]


class Position_only_x(TypedDict, total=True):
    x: int | float | str


class Position_only_y(TypedDict, total=True):
    y: int | float | str


class Position_only(Position_only_x, Position_only_y):
    pass


class Annotation(TypedDict, total=False):
    annotation: str


class Position(Position_only, Annotation):
    pass


class Position_x(Position_only_x, Annotation):
    pass


class Positions_only_x(TypedDict, total=True):
    x: list[int] | list[float] | list[str]


class Positions_only_y(TypedDict, total=True):
    y: list[int | float | str]


class Positions_only(Positions_only_x, Positions_only_y):
    pass


class Annotations(TypedDict, total=False):
    annotation: list[str]


class Positions_list(Positions_only, Annotations):
    pass


class Positions_list_x(Positions_only_x, Annotations):
    pass


class result_of_factorized_and_split(TypedDict):
    inequations: tuple[tuple[Inequation, Inequation],
                       tuple[Inequation, Inequation]] | None
    relation_index: Literal[0, 1, 2, 3]


plotRange = AdapterTypes.plotRange

plotRanges = dict[str, plotRange]

plotRange_2d = tuple[plotRange, plotRange]

relation_content = symbol_condition | Term | MathConditional | Solutions | VectorEquation | VectorSolutions | Vector

# equation_list_row = list[tuple[term_, term_]]
# vector_tuple_row = tuple[list[term_], list[term_]]
# row_solutions = list[tuple[Formula, list[term_]]]


astElement = AdapterTypes.astElement
