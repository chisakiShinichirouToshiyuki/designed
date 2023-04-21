# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from typing import Any
from typing import Literal
from typing import TYPE_CHECKING
from typing import TypedDict
from fractions import Fraction as NativeFraction
from .証明クラス import 証明クラス
from .座標クラス import 座標クラス
from .図形クラス import 図形クラス
from .範囲クラス import 範囲クラス
from .方程式クラス import 定義式クラス
from .方程式クラス import 説明式クラス
from .方程式ずクラス import 方程式ずクラス
from .方程式ずクラス import ベクトル方程式クラス
from .方程式ずクラス import 解ずクラス

from .章クラス import 章クラス
from .マークダウンコンテンツクラス import マークダウンコンテンツクラス
from .関係コンテンツクラス import 関係コンテンツクラス
from .数理的真偽クラス import 数理的真偽クラス
from .数理的命題クラス import 数理的命題クラス
from .数理的命題クラス import 数理的命題クラス
# from 項クラス import 項クラス
from .抽象木クラス import 抽象木クラス
from .Set import Set
from .整数クラス import 整数クラス
from .有限小数クラス import 有限小数クラス
from .分数クラス import 分数クラス
from .式クラス import 式クラス
from .ベクトルクラス import ベクトルクラス
from .ベクトルクラス import 整数ペアクラス
from .ベクトルクラス import 自然数ペアクラス
from .方程式クラス import 方程式クラス
from .非等式クラス import 非等式クラス
from .ベクトル解ずクラス import ベクトル解ずクラス
from .不等式クラス import 不等式クラス
from .不等式クラス import 不等式_v1クラス
from .不等式クラス import 不等式_v2クラス
from .複合条件クラス import 複合条件クラス
from .複合条件クラス import 複合条件_v1クラス
from .複合条件クラス import 複合条件_v2クラス
from .図形登録クラス import 図形登録クラス
from .ベン図登録クラス import ベン図登録クラス
from .テーブルクラス import テーブルクラス

定義式クラス = 定義式クラス
説明式クラス = 説明式クラス
方程式ずクラス = 方程式ずクラス
図形クラス = 図形クラス
座標クラス = 座標クラス
抽象木クラス = 抽象木クラス
Set = Set
範囲クラス = 範囲クラス
数理的条件クラス =  Union[方程式クラス , 不等式クラス , 非等式クラス , 複合条件クラス , 数理的真偽クラス] 
項クラス =  Union[式クラス , 有限小数クラス , 整数クラス , 分数クラス] 


# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import _ad as AdapterTypes


class subtract_prime_result(TypedDict):
    項: 式クラス
    signInteger: Literal[1, -1]


class Modee(TypedDict):
    residual: int
    power: int


# Independent type
markdown_str = str
整数候補 =  Union[整数クラス , 式クラス] 
整数候補_インプット =  Union[int , 整数候補] 
整数ペア_インプット = tuple[整数候補_インプット, 整数候補_インプット]
integer_pair = tuple[整数候補, 整数候補]
condition_symbol = Literal['True', 'False']
number_symbol = Literal['oo', '-oo']
equation_symbol_ = Literal['=']
hsla = tuple[ Union[float , int] ,  Union[float , int] ,  Union[float , int] ,  Union[float ,
             int] ] | tuple[ Union[float , int] ,  Union[float , int] ,  Union[float , int] ]
不等関係 = Literal['<', '<=', '>', '>=']
inequation_symbol = Literal['<', '<=', '>', '>=']
term_type = type[整数クラス] | type[有限小数クラス] | type[分数クラス] | type[式クラス]
テーブルdata = dict[str, list[ Union[str , int , float] ]]
unequation_symbol = Literal['!=']
variable_symbol = Any
plotRange_ = tuple[tuple[ Union[int , float] ,  Union[int , float] ],
                   tuple[ Union[int , float] ,  Union[int , float] ]]
# Dependent type
演算子 = Literal[AdapterTypes.operator_symbol, number_symbol,
                               condition_symbol, equation_symbol_, inequation_symbol, unequation_symbol]
symbol_type = Literal[演算子, 'symbol', condition_symbol]
type_from_term_inequation = \
    type[数理的真偽クラス] | type[不等式クラス] | type[不等式_v1クラス] | type[不等式_v2クラス] | type[方程式クラス] | type[
        非等式クラス] | type[複合条件クラス] | type[複合条件_v1クラス] | type[複合条件_v2クラス]
変数ず = dict[str, variable_symbol]
single_condition =  Union[方程式クラス , 非等式クラス , 不等式クラス , 不等式_v1クラス , 不等式_v2クラス , 数理的真偽クラス] 
数理的範囲 =  Union[方程式クラス , 非等式クラス , 不等式クラス , 不等式_v1クラス , 不等式_v2クラス , 複合条件クラス , 複合条件_v1クラス , 複合条件_v2クラス] 
数理的コンディション =  Union[数理的範囲 , 数理的真偽クラス] 

# Independent type


class squared_result(TypedDict):
    square: 式クラス
    correction_term: 式クラス


class add_and_subtract_products_equation(TypedDict):
    left_plus_term: 式クラス
    left_minus_term: 式クラス
    right_constant_term:  Union[整数クラス , 分数クラス] 


class euclidean_output_each_process(TypedDict):
    result: 自然数ペアクラス
    説明: 章クラス


class euclidean_output(TypedDict):
    result:  Union[自然数ペアクラス , 整数候補] 
    説明: 章クラス


class 変数タイプオプション(TypedDict, total=False):
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


class 方程式(TypedDict):
    formula_left: str
    formula_right: str


class ベン図data(TypedDict):
    label: str
    set: set[int] | set[str]
# Dependent type


変数タイプずオプション = dict[str, 変数タイプオプション]
説明 =  Union[章クラス , 関係コンテンツクラス , str , マークダウンコンテンツクラス , テーブルクラス , 図形登録クラス , ベン図登録クラス] 


class common_initialize_result(TypedDict):
    証明: 証明クラス
    抽象木: AdapterTypes.抽象木要素
    変数ず: set[str]


class equation_symbol(TypedDict):
    formula_left: variable_symbol
    formula_right: variable_symbol


class checked_variable(TypedDict):
    existed_variables: 変数ず
    added_variables: set[str]


class condition(TypedDict):
    times: int
    mod: list[int]


項_インスタンス =  Union[float , int]  | 整数クラス | 有限小数クラス | 分数クラス | 式クラス
conditions_float = dict[str, float]
conditions_int = dict[str, int]
conditions_str = dict[str, str]
conditions_term = dict[str, 項クラス]
conditions_fraction = dict[str, NativeFraction]
conditions_native =  Union[conditions_float , conditions_int , conditions_str] 
term_ = 項クラス |  Union[float , int]  | NativeFraction
項 = 項クラス | str |  Union[float , int]  | NativeFraction
hex_rgb = tuple[int, int, int]
プロットカラー = Literal[
    'black',
    'red',
    'green',
    'orange'
]


class Position_only_x(TypedDict, total=True):
    x:  Union[int , float]  | str


class Position_only_y(TypedDict, total=True):
    y:  Union[int , float]  | str


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
    y: list[ Union[int , float]  | str]


class Positions_only(Positions_only_x, Positions_only_y):
    pass


class Annotations(TypedDict, total=False):
    annotation: list[str]


class Positions_list(Positions_only, Annotations):
    pass


class Positions_list_x(Positions_only_x, Annotations):
    pass


class result_of_factorized_and_split(TypedDict):
    inequations: tuple[tuple[不等式クラス, 不等式クラス],
                       tuple[不等式クラス, 不等式クラス]] | None
    relation_index: Literal[0, 1, 2, 3]


プロット範囲 = AdapterTypes.プロット範囲

プロット範囲ず = dict[str, プロット範囲]

プロット範囲_2次 = tuple[プロット範囲, プロット範囲]

関係コンテンツ =  Union[数理的コンディション , 項クラス , 数理的命題クラス , 解ずクラス , ベクトル方程式クラス , ベクトル解ずクラス , ベクトルクラス] 

# equation_list_row = list[tuple[term_, term_]]
# vector_tuple_row = tuple[list[term_], list[term_]]
# row_solutions = list[tuple[式クラス, list[term_]]]


抽象木要素 = AdapterTypes.抽象木要素
