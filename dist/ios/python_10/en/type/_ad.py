# pyright: reportUnusedImport=false
from __future__ import annotations
from typing import Any, Literal, TypedDict

hex_rgb = tuple[int, int, int]

hsl = tuple[float | int, float | int, float | int]
hsla_full = tuple[float | int, float | int, float | int, float |int]
hsla = hsla_full  | hsl

plot_color = Literal[
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan',
    'darkgoldenrod',
    'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet',
    'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew',
    'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen',
    'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
    'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown',
    'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'
]

plotRange = tuple[int | float, int | float]

plotRanges = dict[str, plotRange]

plotRange_2d = tuple[plotRange, plotRange]




# plotRange= tuple[int|float, int|float]

# plotRanges = dict[str, plotRange]

# plotRange_2d = tuple[plotRange,plotRange]

range_v1 = tuple[int | float, int | float]
range_v2 = tuple[tuple[int | float, int | float],
                 tuple[int | float, int | float]]

variable_symbol = Any
formula_symbol = Any
variables = dict[str, variable_symbol]


class equation(TypedDict):
    formula_left: str
    formula_right: str


operator_symbol = Literal['+', '*', '**', '%', 'log', '/',
                         'sin', 'cos', 'tan', '&', '~', '|', 'setInterval', 'setIntervalUnion','UniversalSet', 'finite_set', '||', 'floor','sols']
                        #  'sin', 'cos', 'tan', '&', '~', '|', 'setInterval', 'setIntervalUnion', 'finite_set', '||', 'floor','sols']
number_symbol = Literal['oo', '-oo']
equationSymbol = Literal['=']
conditionSymbol = Literal['True', 'False']
inequationSymbol = Literal['<', '<=', '>', '>=']
unequationSymbol = Literal['!=']
symbolRelationType = Literal[operator_symbol, number_symbol, conditionSymbol,
                             equationSymbol, inequationSymbol, unequationSymbol]
symbolType = Literal[symbolRelationType, 'symbol', conditionSymbol]


class vennData(TypedDict):
    label: str
    set: set[int] | set[str]


class plotRange_eachVariable(TypedDict):
    min: int | float
    max: int | float
    symbol: str


sympyClass = Literal[
    "<class 'sympy.core.add.Add'>",
    "<class 'sympy.core.mul.Mul'>",
    "<class 'sympy.core.numbers.Half'>",
    "<class 'sympy.core.numbers.Infinity'>",
    "<class 'sympy.core.numbers.NegativeInfinity'>",
    "<class 'sympy.core.numbers.Rational'>",
    "<class 'sympy.core.power.Pow'>",
    "<class 'sympy.core.relational.Equality'>",
    "<class 'sympy.core.relational.GreaterThan'>",
    "<class 'sympy.core.relational.LessThan'>",
    "<class 'sympy.core.relational.StrictGreaterThan'>",
    "<class 'sympy.core.relational.StrictLessThan'>",
    "<class 'sympy.core.relational.Unequality'>",
    "<class 'sympy.sets.sets.EmptySet'>",
    "<class 'sympy.sets.sets.FiniteSet'>",
    "<class 'sympy.sets.sets.Interval'>",
    "<class 'sympy.sets.sets.Union'>",
    "<class 'sympy.sets.sets.UniversalSet'>",
    "<class 'sympy.logic.boolalg.BooleanFalse'>",
    "<class 'sympy.logic.boolalg.BooleanTrue'>",
    # "<class 'sympy.polys.rootoftools.ComplexRootOf'>",
    "Abs",
    "And",
    "cos",
    "floor",
    "log",
    "Mod",
    "Not",
    "Or",
    "sin",
    "tan",
]


sympyFunction2Operator: dict[sympyClass, symbolRelationType] = {
    "<class 'sympy.core.add.Add'>": '+',
    "<class 'sympy.core.mul.Mul'>": '*',
    "<class 'sympy.core.numbers.Half'>": '/',
    "<class 'sympy.core.numbers.Infinity'>": 'oo',
    "<class 'sympy.core.numbers.NegativeInfinity'>": '-oo',
    "<class 'sympy.core.numbers.Rational'>": '/',
    "<class 'sympy.core.power.Pow'>": '**',
    "<class 'sympy.core.relational.Equality'>": '=',
    "<class 'sympy.core.relational.GreaterThan'>": '>=',
    "<class 'sympy.core.relational.LessThan'>": '<=',
    "<class 'sympy.core.relational.StrictLessThan'>": '<',
    "<class 'sympy.core.relational.StrictGreaterThan'>": '>',
    "<class 'sympy.core.relational.Unequality'>": '!=',
    "<class 'sympy.sets.sets.EmptySet'>": 'finite_set',
    "<class 'sympy.sets.sets.FiniteSet'>": 'finite_set',
    "<class 'sympy.sets.sets.Interval'>": 'setInterval',
    "<class 'sympy.sets.sets.Union'>": 'setIntervalUnion',
    "<class 'sympy.sets.sets.UniversalSet'>": 'UniversalSet',
    "<class 'sympy.logic.boolalg.BooleanFalse'>": 'False',
    "<class 'sympy.logic.boolalg.BooleanTrue'>": 'True',
    # "<class 'sympy.polys.rootoftools.ComplexRootOf'>":'sols',
    "Abs": '||',
    "And": '&',
    "cos": 'cos',
    "floor": 'floor',
    "log": 'log',
    "Mod": '%',
    "Not": '~',
    "Or": '|',
    "sin": 'sin',
    "tan": 'tan'
}


class astElement(TypedDict):
    type: Literal['function', 'symbol', 'condition']
    name: symbolType
    text: str
    argumentsLength: int
    arguments: list[astElement]


class variableType(TypedDict):
    real: bool
    integer: bool
    rational: bool
    positive: bool


class variableType_optional(TypedDict, total=False):
    real: Literal[True]
    integer: Literal[True]
    rational: Literal[True]
    positive: Literal[True]

