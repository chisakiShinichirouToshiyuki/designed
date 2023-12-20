from __future__ import annotations
from typing import Any, Union, Literal, TypedDict, overload, Optional, List
from abc import ABCMeta, abstractmethod
from typing import Generator
from typing import Callable
import pandas as pd
from markdown import Markdown
from IPython.core.display import Markdown as Markdown, Math as Math
from fractions import Fraction as NativeFraction

##### ./wip/designed/plot_adapter.py #####

class プロットアダプタークラス:
    @staticmethod
    def 追加する_カラム(
        データフレーム: pd.DataFrame, カラム名: str | int | float, ボディ: list[str | int | float]
    ) -> None: ...
    @staticmethod
    def 表示する_テーブル(データフレーム: pd.DataFrame) -> type["プロットアダプタークラス"]: ...
    @staticmethod
    def 解除する_表示制限(向き: Literal["row", "column"]) -> None: ...
    @staticmethod
    def 設定する_テーブルインデックス(データフレーム: pd.DataFrame, カラム名: str | int | float) -> None: ...

class plotRangeClass(TypedDict):
    min: float | int
    max: float | int

variables = dict[str, variable_symbol]

class 座標ベースクラス:
    def __init__(self, ax: Any) -> None: ...

class 図形ベースクラス:
    def __init__(
        self,
        row_column: tuple[int, int],
        size: tuple[int | float, int | float] = (15, 7.5),
        title: str = "",
    ) -> None: ...
    def 表示する(self) -> 図形ベースクラス: ...

##### ./wip/designed/_ad.py #####

hex_rgb = tuple[int, int, int]
hsl = tuple[float | int, float | int, float | int]
hsla_full = tuple[float | int, float | int, float | int, float | int]
hsla = hsla_full | hsl
plot_color = Literal[
    "aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "black",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkgrey",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkslategrey",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dimgrey",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "green",
    "greenyellow",
    "grey",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgoldenrodyellow",
    "lightgray",
    "lightgreen",
    "lightgrey",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightslategray",
    "lightslategrey",
    "lightsteelblue",
    "lightyellow",
    "lime",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "rebeccapurple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "slategrey",
    "snow",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen",
]
plotRange = tuple[int | float, int | float]
plotRanges = dict[str, plotRange]
plotRange_2d = tuple[plotRange, plotRange]
range_v1 = tuple[int | float, int | float]
range_v2 = tuple[tuple[int | float, int | float], tuple[int | float, int | float]]
variable_symbol = Any
formula_symbol = Any

class equation(TypedDict):
    formula_left: str
    formula_right: str

operator_symbol = Literal[
    "+",
    "*",
    "**",
    "%",
    "log",
    "/",
    "sin",
    "cos",
    "tan",
    "&",
    "~",
    "|",
    "setInterval",
    "setIntervalUnion",
    "UniversalSet",
    "finite_set",
    "||",
    "floor",
    "sols",
]
#  'sin', 'cos', 'tan', '&', '~', '|', 'setInterval', 'setIntervalUnion', 'finite_set', '||', 'floor','sols']
number_symbol = Literal["oo", "-oo"]
equationSymbol = Literal["="]
conditionSymbol = Literal["True", "False"]
inequationSymbol = Literal["<", "<=", ">", ">="]
unequationSymbol = Literal["!="]
symbolRelationType = Literal[
    operator_symbol,
    number_symbol,
    conditionSymbol,
    equationSymbol,
    inequationSymbol,
    unequationSymbol,
]
symbolType = Literal[symbolRelationType, "symbol", conditionSymbol]

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
sympyFunction2Operator: dict[sympyClass, symbolRelationType]

class astElement(TypedDict):
    type: Literal["function", "symbol", "condition"]
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

##### ./wip/designed/ast.py #####

class 抽象構文木クラス:
    """
    数式の抽象構文木を表現するクラス。

    数式の解析に使います。

    Attributes:
        _proof: 証明に関する情報を含むオブジェクト。

        __ast: 抽象構文木のメインデータ。

        __ast_not_evaluated: 評価されていない抽象構文木。

        __variable_types: 変数の型情報。
    """

    def __init__(
        self,
        proof: 証明クラス,
        express: str,
        assertee_function: list[symbol_type] = [],
        variable_types: variable_type_optional | variable_types_optional = {},
    ) -> None:
        """
        抽象構文木クラス インスタンスを初期化します。

        Args:
            proof (証明クラス): 証明に関する情報。

            express (str): 解析する数式の文字列。

            assertee_function (list[symbol_type], optional): 断定する関数のリスト。デフォルトは空のリスト。

            variable_types (variable_type_optional | variable_types_optional, optional): 変数の型情報。デフォルトは空の辞書。
        """
        ...
    def 検証する_関数(self, 検証対象の関数: list[symbol_type], 逆順で検索をするか: bool = False) -> 抽象構文木クラス:
        """
            数式に対して機能を適用します。

        Args:
            assert_function (list[symbol_type]): 断定する関数のリスト。

            should_regressive_search (bool, optional): 逆順で検索するかどうか。デフォルトは False。


        Returns:
            抽象構文木クラス: 自分自身を返す。
        """
        ...
    @property
    def 抽象構文木_因数分解のための整形された不等式(self) -> astElement:
        """
            数式を因数分解のための形式に変換した抽象構文木を返します。

        Returns:
            astElement: 因数分解のために整形された抽象構文木。
        """
        ...
    @property
    def 要素(self) -> astElement: ...
    @property
    def 要素_未評価(self) -> astElement:
        """
            このインスタンスの数式の抽象構文木を返します。

        Returns:
            astElement: 抽象構文木。
        """
        ...
    @property
    def 評価(self) -> astElement:
        """
            数式の抽象構文木を評価した結果を返します。

        Returns:
            astElement: 評価された抽象構文木。
        """
        ...
    @property
    def 要素s(self) -> list[str]:
        """
            数式の要素を取得します。

        Returns:
            list[str]: 数式の要素のリスト。
        """
        ...
    def 取得する_末端の葉s(
        self,
        抽象構文木: astElement | None = None,
        葉のタイプ: list[symbol_relation_type] = [],
        葉s: list[astElement] = [],
    ) -> list[astElement]:
        """
            抽象構文木の末端のノードを取得します。

        Parameters:
            ast (astElement, 任意): 解析する抽象構文木。Noneの場合は、ast_prettified_inequation_for_factorizeを使用します。

            leaf_type (list[symbol_relation_type], 任意): 取得する末端ノードのタイプのリスト。最初は空のリスト。

            leafs (list[astElement], 任意): 既存の末端ノードのリスト。最初は空のリスト。


        Returns:
            list[astElement]: 末端のノードのリスト。
        """
        ...
    @staticmethod
    def 取得する_プロット可能な条件リスト(
        抽象構文木: astElement,
        すべての変数s: variables,
        条件s: list[astElement] = [],
    ) -> list[astElement]:
        """
            抽象構文木(ast)からプロット可能な条件を抽出します。

        Parameters:
            ast (astElement): 解析する抽象構文木

            all_variables (variables): すべての変数を含むオブジェクト。

            conditions (list[astElement], 任意): 既存の条件のリスト。最初は空のリスト。


        Returns:
            list[astElement]: プロット可能な条件のリスト。
        """
        ...
    def 取得する_べき乗項(self, 抽象構文木: astElement | None = None) -> list[str]:
        """
            指定された抽象構文木からべき乗の項を抽出します。

        Parameters:
            ast (astElement, 任意): 解析する抽象構文木。Noneの場合は、elementプロパティを使用します。

        Returns:
            list[str]: べき乗の項のリスト。
        """
        ...
    @property
    def テキスト(self) -> str:
        """
            抽象構文木をテキスト形式で取得します。

        Returns:
            str: 抽象構文木のテキスト形式。
        """
        ...
    @property
    def 変数s(self) -> set[str]:
        """
            式中の変数を取得します。

        Returns:
            set[str]: 式中の変数の集合。
        """
        ...

##### ./wip/designed/ax.py #####

class 座標クラス(座標ベースクラス):
    def __init__(self, figure: 図形クラス, ax: Any) -> None: ...
    def 追加する_グリッド(self) -> 座標クラス: ...
    def プロットする_条件(
        self,
        条件: SymbolCondition,
        軸s: list[str] | None = None,
        色: hsla | None = None,
    ) -> 座標クラス: ...
    def プロットする_直線の式(
        self,
        式: 式クラス | str | float | int | NativeFraction,
        変数: str,
        色: hsla = (220, 100, 50),
        ラベル: str = "",
    ) -> 座標クラス: ...
    def プロットする_散布の式(
        self,
        データ: list[Position_x] | Positions_list_x,
        式: 式クラス | str | float | int | NativeFraction,
        変数: str,
        色: plot_color | hex_rgb = "black",
        ラベル: str = "",
    ) -> 座標クラス: ...
    def プロットする_散布点(
        self,
        データ: list[Position] | Positions_list,
        色: plot_color | hex_rgb,
    ) -> 座標クラス: ...
    def リセットする_ラベル(self, ラベルs: tuple[str, str]) -> 座標クラス: ...
    def リセットする_プロットのプロパティ(
        self, プロパティ: Literal["dot_radius", "line_width", "z_oder"], 値: float | int
    ) -> 座標クラス: ...
    def リセットする_範囲(self, 範囲: plotRange_2d) -> 座標クラス:
        """
            グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        ...
    def リセットする_タイトル(self, タイトル: str) -> 座標クラス:
        """
            グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        ...
    def 設定する_凡例(self) -> 座標クラス: ...

##### ./wip/designed/complex_condition.py #####

class 複合条件クラス:
    def __init__(self, proof: 証明クラス, express: str) -> None: ...
    def __invert__(self) -> symbol_condition: ...
    def __and__(self, other: bool | symbol_condition) -> symbol_condition:
        """
        論理和の中置演算子

        Args:
            other : 演算対象
        """
        ...
    def __or__(self, other: bool | symbol_condition) -> symbol_condition: ...
    def __eq__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ne__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __le__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __gt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ge__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __lshift__(self, other: SymbolCondition) -> 数理命題クラス: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャストできるか(self, タイプ: type_from_term_inequation) -> 数理的ブールクラス: ...
    def キャスト可能なタイプ(self) -> list[type_from_term_inequation]: ...
    def 表示する(self) -> 複合条件クラス: ...
    def 表示する_論理ツリー(self) -> 複合条件クラス: ...
    @property
    def 論理ツリー(self) -> マークダウンコンテンツクラス: ...
    def 作成する_図(
        self,
        プロット範囲s: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順の軸のオーダー: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    def プロットする(
        self,
        プロット範囲s: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順の軸のオーダー: bool = True,
        タイトル: str = "",
    ) -> 複合条件クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

class 複合条件_v1クラス(複合条件クラス):
    def __init__(self, proof: 証明クラス, express: str) -> None: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def __sub__(self, formula: 複合条件_v1クラス) -> 複合条件_v1クラス | 方程式クラス: ...
    def 取得できるか_整数のセット(self, セット限界: int = 1000, エラーを発生させるべきか: bool = False) -> bool: ...
    def キャスト可能なタイプ(self) -> list[type_from_term_inequation]: ...
    def 表示する_範囲(self): ...
    def 取得する_整数のセット(self, セット限界: int = 1000) -> set[int]: ...
    @property
    def 範囲(self) -> markdown_str: ...

class 複合条件_v2クラス(複合条件クラス):
    def __init__(self, proof: 証明クラス, express: str) -> None: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャスト可能なタイプ(self) -> list[type_from_term_inequation]: ...

##### ./wip/designed/conditional.py #####

class 命題クラス(metaclass=ABCMeta):
    def __init__(
        self,
        sufficient_condition: str,
        necessary_condition: str,
        sufficient_condition_bool: bool = True,
        necessary_condition_bool: bool = True,
    ) -> None: ...
    def 追加する_接尾辞(self, セグメント_インデックス: Literal[0, 1], 意見: bool) -> str: ...
    def 分析する_戦略(self) -> 命題クラス: ...
    @property
    @abstractmethod
    def 対偶(self) -> 命題クラス: ...
    @property
    @abstractmethod
    def 逆(self) -> 命題クラス: ...
    @property
    @abstractmethod
    def 裏(self) -> 命題クラス: ...
    @property
    @abstractmethod
    def 反対(self) -> 命題クラス: ...
    @property
    @abstractmethod
    def テキスト(self) -> str: ...
    @property
    def テキスト_対偶(self) -> str: ...
    @property
    def テキスト_逆(self) -> str: ...
    @property
    def テキスト_裏(self) -> str: ...
    @property
    @abstractmethod
    def テキスト_必要条件(self) -> str: ...
    @property
    def テキスト_反対(self) -> str: ...
    @property
    @abstractmethod
    def テキスト_十分条件(self) -> str: ...

##### ./wip/designed/designed_float.py #####

class 浮動小数クラス:
    def __init__(self, proof: 証明クラス, express: float) -> None: ...
    def __eq__(self, other: term_) -> 数理的ブールクラス | 方程式クラス: ...
    def __ne__(self, other: term_) -> 数理的ブールクラス | 非等号クラス: ...
    def __lt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __le__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __gt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __ge__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    @overload
    def __add__(self, formula: float | int | 浮動小数クラス | 整数クラス | 分数クラス) -> 浮動小数クラス: ...
    @overload
    def __add__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __sub__(self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 浮動小数クラス: ...
    @overload
    def __sub__(self, formula: 式クラス) -> 式クラス: ...
    def __neg__(self) -> 浮動小数クラス: ...
    @overload
    def __mul__(self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 浮動小数クラス: ...
    @overload
    def __mul__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __truediv__(
        self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス
    ) -> 浮動小数クラス: ...
    @overload
    def __truediv__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __mod__(self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, formula: 式クラス) -> 式クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, formula: 式クラス) -> 式クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __pow__(
        self,
        formula: 式クラス | float | int | 分数クラス | 整数クラス | 浮動小数クラス,
    ) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __radd__(self, formula: float | int) -> 浮動小数クラス:
        """
        [+] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rsub__(self, formula: float | int) -> 浮動小数クラス:
        """
        [-] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rmul__(self, formula: float | int) -> 浮動小数クラス:
        """
        [*] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rtruediv__(self, formula: float | int) -> 浮動小数クラス:
        """
        [/] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rpow__(self, formula: float | int) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rmod__(self, formula: float | int) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rfloordiv__(self, formula: float | int) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rshift__(self, type: type[整数クラス]) -> 整数クラス: ...
    @overload
    def __rshift__(self, type: type[式クラス]) -> 式クラス: ...
    @overload
    def __rshift__(self, type: type[分数クラス]) -> 分数クラス: ...
    @property
    def 抽象構文木(self) -> 抽象構文木クラス: ...
    def キャストできますか(self, タイプ: type[整数クラス] | type[分数クラス]) -> bool: ...
    @property
    def 次数(self) -> int:
        """
            式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        ...
    def 表示する(self) -> 浮動小数クラス: ...
    def 取得する_係数s(self, フォーカス変数: str, 整数に制限するべきですか: bool = False) -> list[浮動小数クラス]: ...
    @property
    def は整数ですか(self) -> bool | None: ...
    @property
    def 数字(self) -> float: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

##### ./wip/designed/designed_range.py #####

class 範囲クラス:
    def __init__(self, proof: 証明クラス, express: str) -> None: ...
    def __or__(self, formula: 範囲クラス) -> 集合クラス | 範囲クラス: ...
    def __and__(self, formula: 範囲クラス) -> 集合クラス | 範囲クラス: ...
    def __sub__(self, formula: 範囲クラス) -> 集合クラス | 範囲クラス: ...
    def __eq__(self, formula: 範囲クラス) -> bool: ...
    def __ne__(self, formula: 範囲クラス) -> bool: ...
    def __lt__(self, formula: 範囲クラス) -> bool: ...
    def __le__(self, formula: 範囲クラス) -> bool: ...
    def __gt__(self, formula: 範囲クラス) -> bool: ...
    def __ge__(self, formula: 範囲クラス) -> bool: ...
    def __format__(self, __format_spec: str) -> markdown_str: ...
    def 集合化する(self, 変数: str) -> 集合クラス: ...
    @property
    def 抽象構文木(self) -> 抽象構文木クラス: ...
    def 取得可能か_整数集合(
        self,
        抽象構文木: astElement | None = None,
        集合限界: int = 1000,
        エラーを発生させるべき: bool = False,
    ) -> bool: ...
    def 表示する(self) -> 範囲クラス: ...
    def 取得する_整数集合(
        self, 抽象構文木: astElement | None = None, 集合限界: int = 1000
    ) -> set[int]: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

##### ./wip/designed/designed_set.py #####

class 集合クラス:
    def __init__(
        self,
        proof: 証明クラス,
        express: express_str
        | express_str_set
        | express_int_set
        | express_float_set = set(),
    ) -> None: ...
    def 表示する(self) -> 集合クラス: ...
    @property
    def テキスト(self) -> str: ...

express_str = str
express_str_set = set[str]
express_int_set = set[int]
express_float_set = set[float]

##### ./wip/designed/diophantine_equation_utils.py #####

class 不定方程式ユーティルクラス:
    @staticmethod
    def 取る_不定方程式の解の範囲(
        方程式: 方程式クラス,
        証明: 証明クラス,
        変数サイズの順序: list[str],
        厳密な順序かい: bool = False,
        セクション_タイトル: str = "不定方程式の解の範囲",
        セクション_ID: str = "get_solution_range_of_diophantine_equation",
    ) -> list[不等式クラス]: ...
    @staticmethod
    def 解く_不定方程式_和差の積型(
        証明: 証明クラス,
        方程式: add_and_subtract_products_equation,
        自然数かい: bool = False,
        セクション_タイトル: str = "２乗差の不定方程式の解",
        セクション_ID: str = "解く_不定方程式_和差の積型",
    ) -> ベクトル解sクラス: ...
    @staticmethod
    def 解く_不定方程式_d1_v2(
        方程式: 方程式クラス,
        証明: 証明クラス,
        パラメータ_シンボル: str = "k_",
        検索範囲: tuple[int, int] = (-5, 5),
        セクション_タイトル: str = "１次２変数の不定方程式の解",
        セクション_ID: str = "解く_不定方程式_d1_v2",
    ) -> ベクトル方程式クラス: ...
    @staticmethod
    def 解く_分解型の不定方程式_d1_v2(
        方程式: 方程式クラス,
        証明: 証明クラス,
        セクション_タイトル: str = "１次２変数の不定方程式(分解型)の解",
        セクション_ID: str = "解く_分解型の不定方程式_d1_v2",
    ) -> ベクトル解sクラス: ...
    @staticmethod
    def 解く_分解型不定方程式_d2_v2(
        方程式: 方程式クラス,
        証明: 証明クラス,
        自然数かい: bool = False,
        セクション_タイトル: str = "２次２変数の不定方程式(分解型)の解",
        セクション_ID: str = "解く_分解型不定方程式_d2_v2",
    ) -> ベクトル解sクラス: ...
    @staticmethod
    def 解く_対称不定方程式(
        方程式: 方程式クラス,
        証明: 証明クラス,
        変数サイズの順序: list[str] = [],
        厳密な順序かい: bool = False,
        セクション_タイトル: str = "対称式の不定方程式の解",
        セクション_ID: str = "解く_対称不定方程式",
    ) -> ベクトル解sクラス | None:
        """
            対称不定方程式を解く

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
        ...
    @staticmethod
    def 解く_解く_急増する各辺の差の等式(
        方程式: 方程式クラス,
        証明: 証明クラス,
        スキャン範囲: tuple[int, int] = (0, 10),
        セクション_タイトル: str = "解く_急増する各辺の差の等式の解法",
        セクション_ID: str = "解く_急増する各辺の差の等式",
    ) -> 解sクラス: ...

##### ./wip/designed/equation.py #####

class 方程式クラス:
    def __init__(self, proof: 証明クラス, equation: str | term_pair) -> None: ...
    def __invert__(self) -> symbol_condition:
        """
        sum

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: sum result

        Examples:
            >>> print(testfunc(2,5))
            7
        """
        ...
    def __and__(self, other: bool | symbol_condition) -> symbol_condition:
        """
        論理和の中置演算子

        Args:
            other : 演算対象
        """
        ...
    def __or__(self, other: bool | symbol_condition) -> symbol_condition: ...
    def __eq__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ne__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __le__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __gt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ge__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lshift__(self, other: SymbolCondition) -> 数理命題クラス: ...
    def __add__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [+] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __sub__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [-] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __neg__(self) -> 分数クラス: ...
    def __mul__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [*] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __truediv__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [/] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __pow__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [**] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __radd__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [+] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rsub__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [-] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rmul__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [*] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rtruediv__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [/] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rpow__(
        self,
        equation_or_term: 方程式クラス | Term | int | float | NativeFraction,
    ) -> 方程式クラス:
        """
        [**] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __format__(self, __format_spec: str) -> str: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[定義式クラス]) -> 定義式クラス: ...
    @overload
    def __rshift__(self, type: type[説明式クラス]) -> 説明式クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャストできる(self, タイプ: type_from_term_inequation) -> 数理的ブールクラス: ...
    def キャスト可能な型(self) -> list[type_from_term_inequation]: ...
    @property
    def 次数(self) -> int:
        """
            式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        ...
    def 表示する(self, 無加工かい: bool = True) -> 方程式クラス: ...
    @property
    def 評価済み(self) -> 方程式クラス | 数理的ブールクラス: ...
    def 因数分解する(self) -> 方程式クラス: ...
    @property
    def 式s(self) -> tuple[式クラス, 式クラス]: ...
    def 取得する_特殊解_d1_v2(self, 検索範囲: tuple[int, int]) -> dict_int | None: ...
    def 取得する_不定方程式の解の範囲(
        self,
        変数の大小順序: list[str],
        厳密な順序かい: bool = False,
        セクションタイトル: str = "不定方程式の解の範囲",
        セクションID: str = "取得する_不定方程式の解の範囲",
    ) -> list[不等式クラス]: ...
    def 定義式かい(self) -> bool: ...
    def 恒等式かい(self) -> bool: ...
    def 作成する_図(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順軸順: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    def プロットする(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順軸順: bool = True,
        タイトル: str = "",
    ) -> SymbolCondition: ...
    def 解く(self, フォーカスする変数: str | 式クラス) -> ベクトル式クラス: ...
    def 解く_和差の2乗型の不定方程式(
        self,
        方程式: add_and_subtract_products_equation,
        自然数かい: bool = False,
        セクションタイトル: str = "２乗差の不定方程式の解",
        セクションID: str = "解く_和差の2乗型の不定方程式",
    ) -> ベクトル解sクラス: ...
    def 解く_不定方程式_d1_v2(
        self,
        パラメータシンボル: str = "k_",
        検索範囲: tuple[int, int] = (-5, 5),
        セクションタイトル: str = "１次２変数の不定方程式の解",
        セクションID: str = "解く_不定方程式_d1_v2",
    ) -> ベクトル方程式クラス: ...
    def 解く_分解型の不定方程式_d1_v2(
        self, セクションタイトル: str = "１次２変数の不定方程式(分解型)の解", セクションID: str = "解く_分解型の不定方程式_d1_v2"
    ) -> ベクトル解sクラス:
        """
        １次２変数の不定方程式、(x+m)(y+n)=lの形式に分解して、整数解を求める。
        
        引数
        ----------
        セクションタイトル
            本証明を表示した時のセクションタイトル
        セクションID:
            証明クラスに保存されるセクションID。これを用いて表示構成を組み立てる。

        返り値
        -------
        ベクトル解sクラス:
            複数のベクトル方程式の形式でまとめた、変数とその定数解
        """
        ...



    def 解く_分解型不定方程式_d2_v2(
        self,
        自然数かい: bool = False,
        セクションタイトル: str = "２次２変数の不定方程式(分解型)の解",
        セクションID: str = "解く_分解型不定方程式_d2_v2",
    ) -> ベクトル解sクラス: ...
    def 解く_対称不定方程式(
        self,
        変数の大小順序: list[str] = [],
        厳密な順序かい: bool = False,
        セクションタイトル: str = "対称式の不定方程式の解",
        セクションID: str = "解く_対称不定方程式",
    ) -> ベクトル解sクラス | None:
        """
            対称不定方程式を解く

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
        ...
    def 解く_急増する各辺の差の等式(
        self,
        スキャン範囲: tuple[int, int] = (0, 10),
        セクションタイトル: str = "急増する各辺の差の等式の解法",
        セクションID: str = "解く_急増する各辺の差の等式",
    ) -> 解sクラス: ...
    def 代入する(
        self,
        条件: dict_float | dict_int | dict_term | 方程式クラス | 方程式sクラス,
        辺: literal_direction | None = None,
    ) -> 方程式クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 表示用テキスト(self) -> str: ...
    @property
    def 入力用テキスト(self) -> str: ...
    @property
    def 変数(self) -> set[str]:
        """
        式の変数
        """
        ...

class 方程式_2dクラス(方程式クラス):
    def __init__(
        self,
        proof: 証明クラス,
        equation: str | term_pair,
        main_variable: str = "",
    ) -> None: ...
    @property
    def a(self) -> 式クラス: ...
    @property
    def b(self) -> 式クラス: ...
    @property
    def c(self) -> 式クラス: ...
    @property
    def 判別式(self) -> 式クラス: ...
    @property
    def ヴィエタの公式_加算(self) -> 式クラス: ...
    @property
    def ヴィエタの公式_積(self) -> 式クラス: ...

class 説明式クラス(方程式クラス):
    def __init__(self, proof: 証明クラス, equation: str | formula_term_pair) -> None: ...

class 定義式クラス(説明式クラス):
    def __init__(self, proof: 証明クラス, equation: str | formula_term_pair) -> None: ...
    def __format__(self, __format_spec: str) -> str: ...

term_pair = tuple[term, term]
formula_term_pair = tuple[式クラス, term]
dict_float = dict[str, float]
dict_int = dict[str, int]
dict_term = dict[str, Term]
literal_direction = Literal["left", "right"]

##### ./wip/designed/equation_utils.py #####

default_condition: condition

class 方程敷く便利ツールクラス:
    @staticmethod
    def 調整関数(
        証明: 証明クラス,
        方程式: 方程式クラス,
        調整関数記号: Literal["+", "-", "*", "/", "**"],
        方程式または項: 方程式クラス | Term | float | int | NativeFraction,
        右から操作するかい: bool = True,
    ) -> 方程式クラス: ...

##### ./wip/designed/equations.py #####

class 方程式sクラス:
    def __init__(
        self, proof: 証明クラス, equations: express_list | express_tuple
    ) -> None: ...
    def __getitem__(self, index: int) -> 方程式クラス: ...
    def __iter__(self) -> Generator[方程式クラス, None, None]: ...
    def __len__(self) -> int: ...
    def 方程追加する_式(self, 方程式s: list[方程式クラス]) -> 方程式sクラス: ...
    def 追加する(self, 方程式: 方程式クラス) -> 方程式sクラス: ...
    def 表示する(self) -> 方程式sクラス: ...
    @property
    def 方程式s(self) -> list[方程式クラス]: ...
    def 変数を減らす(self, ターゲット変数: str = "", 定義方程式: 方程式クラス | None = None) -> 方程式sクラス: ...
    def 解く(self, フォーカス項s: set[str] = set()) -> ベクトル方程式クラス | None: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

class 解sクラス(方程式sクラス):
    def __init__(
        self,
        proof: 証明クラス,
        equations: list[方程式クラス] | tuple[ベクトルクラス, ベクトルクラス],
    ) -> None: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __add__(self, other: 解sクラス) -> 解sクラス:
        """
        [+] の中置演算子

        引数:
            other: ベクトルクラス
        結果:
            ベクトルクラス
        """
        ...
    def 表示する(self) -> 解sクラス: ...
    def ソートする(self, 逆転するべき: bool = False) -> 解sクラス: ...

class ベクトル方程式クラス(方程式sクラス):
    def __init__(
        self,
        proof: 証明クラス,
        equations: list[方程式クラス] | tuple[ベクトルクラス, ベクトルクラス],
    ) -> None: ...
    def __eq__(self, other: ベクトル方程式クラス) -> bool: ...
    def __format__(self, __format_spec: str) -> str: ...
    def 方程追加する_式(self, 方程式s: list[方程式クラス]) -> ベクトル方程式クラス: ...
    def 追加する(self, 方程式: 方程式クラス) -> ベクトル方程式クラス: ...
    def 表示する(self) -> ベクトル方程式クラス: ...
    @property
    def 左側のベクトル(self) -> ベクトルクラス: ...
    @property
    def 右側のベクトル(self) -> ベクトルクラス: ...
    def ソートする(self, 逆転するべき: bool = False) -> ベクトル方程式クラス: ...

express_list = list[方程式クラス]
express_tuple = tuple[ベクトルクラス, ベクトルクラス]

##### ./wip/designed/figure.py #####

class 図形クラス(図形ベースクラス):
    def __init__(
        self,
        proof: 証明クラス,
        row_column: tuple[int, int],
        unit_size: tuple[int | float, int | float] = (5, 5),
        title: str = "",
    ) -> None: ...
    def 追加する_サブプロット(self, 行_列: tuple[int, int]) -> 図形クラス: ...
    @property
    def 軸s(self) -> list[list[座標クラス]]: ...
    def 表示する(self) -> 図形クラス: ...
    @property
    def 証明(self) -> 証明クラス: ...

##### ./wip/designed/figure_reservation.py #####

class 図登録クラス:
    def __init__(
        self,
        express: SymbolCondition | 式クラス,
        plot_ranges: plotRange | plotRanges | plotRange_2d | None,
        alphabetic_axis_order: bool = True,
        title: str = "",
    ) -> None: ...
    def 表示する(self): ...

##### ./wip/designed/formula.py #####

class 式クラス:
    def __init__(
        self,
        proof: 証明クラス,
        text: str | float | int,
        variable_types: variable_type_optional | variable_types_optional = {},
    ) -> None: ...
    def __lt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __le__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __gt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __ge__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __add__(
        self,
        other: float | int | 整数クラス | 浮動小数クラス | 分数クラス | 式クラス,
    ) -> 式クラス:
        """
        [+] の中置演算子

        引数:
            other: 演算子の左側の式
        結果:
            式クラス
        """
        ...
    def __sub__(
        self,
        other: 式クラス | float | int | 分数クラス | 整数クラス | 浮動小数クラス,
    ) -> 式クラス:
        """
        [-] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __neg__(self) -> 式クラス: ...
    def __mul__(
        self,
        other: 式クラス | float | int | 分数クラス | 整数クラス | 浮動小数クラス,
    ) -> 式クラス:
        """
        [*] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __truediv__(
        self,
        other: 式クラス | float | int | 分数クラス | 整数クラス | 浮動小数クラス,
    ) -> 式クラス:
        """
        [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __pow__(
        self,
        other: 式クラス | float | int | 分数クラス | 整数クラス | 浮動小数クラス,
    ) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __mod__(self, other: 式クラス | float | int | 整数クラス | 浮動小数クラス) -> 式クラス:
        """
        [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __floordiv__(self, other: 式クラス | float | int | 整数クラス | 浮動小数クラス) -> 式クラス:
        """
        [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __radd__(self, other: float | int) -> 式クラス:
        """
        [+] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rsub__(self, other: float | int) -> 式クラス:
        """
        [-] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rmul__(self, other: float | int) -> 式クラス:
        """
        [*] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rtruediv__(self, other: float | int) -> 式クラス:
        """
        [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rpow__(self, other: float | int) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rmod__(self, other: float | int) -> 式クラス:
        """
        [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rfloordiv__(self, other: float | int) -> 式クラス:
        """
        [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __eq__(self, other: str) -> str: ...
    @overload
    def __eq__(self, other: term_) -> 数理的ブールクラス | 方程式クラス: ...
    @overload
    def __ne__(self, other: str) -> str: ...
    @overload
    def __ne__(self, other: term_) -> 数理的ブールクラス | 非等号クラス: ...
    @overload
    def __rshift__(self, type: type[整数クラス]) -> 整数クラス: ...
    @overload
    def __rshift__(self, type: type[浮動小数クラス]) -> 浮動小数クラス: ...
    @overload
    def __rshift__(self, type: type[分数クラス]) -> 分数クラス: ...
    @property
    def 抽象構文木(self) -> 抽象構文木クラス: ...
    def キャスト可能か(
        self,
        タイプ: type[整数クラス] | type[浮動小数クラス] | type[分数クラス],
    ) -> bool: ...
    def チェックする_対称性(self) -> 数理的ブールクラス: ...
    def チェックする_演算子(self, チェック演算子: list[symbol_type]) -> 数理的ブールクラス: ...
    @property
    def 平方完成(self) -> squared_result: ...
    @property
    def 次数(self) -> int: ...
    def 微分する(self, 注目変数: Union[str, 式クラス, None] = None) -> 式クラス: ...
    def 表示する(self) -> 式クラス: ...
    def 展開する(self) -> 式クラス: ...
    def 因数分解する(self) -> 式クラス:
        """
        caution!: 数字のみの項のある因数分解は失敗するlx:(4+4*x)。sympifyで変換する際に、4*(1+x)が展開されてしまう。代わりに、factorized_elementsを使用する
        """
        ...
    @property
    def 因数分解された要素(self) -> list[式クラス]:
        """
        因数分解の因数(次数なし)
        """
        ...
    def 代入する_不安定(self, 代入するもの: tuple[str, 式クラス]) -> 式クラス: ...
    def 取得する_係数s(self, フォーカス変数: str, 整数を制限する必要があるかい: bool = False) -> list[式クラス]: ...
    def 取得する_因子s(self) -> list[式クラス]: ...
    def 同定する_条件から(
        self,
        除数の量: int,
        範囲: tuple[int, int],
        セクションタイトル: str = "同定する_条件から",
        セクションID: str = "同定する_条件から",
    ) -> ベクトルクラス: ...
    def 積分する(self, フォーカス変数: Union[str, 式クラス, None] = None) -> 式クラス: ...
    @property
    def 整数である(self) -> bool | None: ...
    def ラフチェックする_整数(self, 大まかな検索: bool = False, 正のみ: bool = True) -> bool | None: ...
    def チェックする_互いに素か(
        self,
        その他: 整数クラス | int | 式クラス,
        相対的な素数のペア: List[tuple[int | 整数クラス | 式クラス, int | 整数クラス | 式クラス]] = [],
    ) -> bool | None: ...
    def チェックする_特定の倍数か(
        self,
        回数: int,
        期待される剰余: list[int],
        条件: condition = {"times": 0, "mod": [0]},
        セクションタイトル: str = "チェックする_特定の倍数か",
    ) -> bool: ...
    def 作成する_図(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None = None,
        タイトル: str = "",
    ) -> 図形クラス: ...
    def 単一変数化する(self, ターゲット変数: str) -> 式クラス: ...
    def プロットする(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None = None,
        タイトル: str = "",
        色: hsla = (220, 100, 50),
        ラベル: str = "",
    ) -> 式クラス: ...
    def 証明する_乗数のモジュール性(
        self, モッド: int, セクションタイトル: str = "乗数のモジュール性の証明", セクションID: str = "証明する_乗数のモジュール性"
    ) -> 式クラス: ...
    def ラフチェックする_単調増加(
        self, ポイントs: Optional[list[int]], 自然数内かい: bool = True
    ) -> bool | None: ...
    def 解く(self, フォーカス変数: Union[str, 式クラス, None] = None) -> ベクトル式クラス: ...
    def 代入する(
        self,
        条件: conditions_float
        | conditions_int
        | conditions_str
        | conditions_term
        | 方程式クラス
        | 方程式sクラス,
    ) -> 式クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def テキスト_因数分解後(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

##### ./wip/designed/formula_utils.py #####

class 式便利ツールクラス:
    @staticmethod
    def 左の関数を調整する(
        証明: 証明クラス,
        数式: 式クラス,
        調整関数: Callable[[variables, str, str | int | float], str],
        他の: 整数クラス | int | 浮動小数クラス | float | 分数クラス | 式クラス,
    ) -> 式クラス: ...
    @staticmethod
    def 演算する_右(
        証明: 証明クラス,
        数式: 式クラス,
        調整関数: Callable[[variables, str, str | int | float], str],
        他の: 整数クラス | int | 浮動小数クラス | float | 分数クラス | 式クラス,
    ) -> 式クラス: ...
    @staticmethod
    def 同定する_条件から(
        証明: 証明クラス,
        数式: 式クラス,
        除数の数量: int,
        範囲: tuple[int, int],
        セクションタイトル: str = "整数の特定",
        セクションID: str = "同定する_条件から",
    ) -> ベクトルクラス: ...
    @staticmethod
    def チェックする_特定の倍数か(
        証明: 証明クラス,
        数式: 式クラス,
        回数: int,
        期待されるmod: list[int],
        条件: condition = {"times": 0, "mod": [0]},
        セクションタイトル: str = "チェックする_特定の倍数か",
    ) -> bool: ...
    @staticmethod
    def 証明する_乗数のモジュール性(
        証明: 証明クラス,
        数式: 式クラス,
        mod: int,
        セクションタイトル: str = "乗数のモジュール性の証明",
        セクションID: str = "証明する_乗数のモジュール性",
    ) -> type["式便利ツールクラス"]: ...
    @staticmethod
    def 代入する(
        証明: 証明クラス,
        数式: 式クラス,
        条件s: conditions_float
        | conditions_int
        | conditions_str
        | conditions_term
        | 方程式クラス
        | 方程式sクラス,
    ) -> 式クラス: ...
    @staticmethod
    def プライムを減算する(証明: 証明クラス, 項: astElement) -> subtract_prime_result: ...
    @staticmethod
    def 項を減算する(
        証明: 証明クラス, 数式: 式クラス, 他の: 式クラス
    ) -> tuple[subtract_prime_result, subtract_prime_result]: ...

##### ./wip/designed/fraction.py #####

class 分数クラス:
    def __init__(self, proof: 証明クラス, express: str | express_fraction) -> None: ...
    def __eq__(self, other: term_) -> 数理的ブールクラス | 方程式クラス: ...
    def __ne__(self, other: term_) -> 数理的ブールクラス | 非等号クラス: ...
    def __lt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __le__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __gt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __ge__(self, other: term_) -> 数理的ブールクラス | 不等式クラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    @overload
    def __rshift__(self, type: type[浮動小数クラス]) -> 浮動小数クラス: ...
    @overload
    def __rshift__(self, type: type[式クラス]) -> 式クラス: ...
    @overload
    def __rshift__(self, type: type[整数クラス]) -> 整数クラス: ...
    @overload
    def __add__(self, formula: 整数クラス | int | 分数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __add__(self, formula: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __add__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __sub__(self, formula: 整数クラス | int | 分数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __sub__(self, formula: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __sub__(self, formula: 式クラス) -> 式クラス: ...
    def __neg__(self) -> 分数クラス: ...
    @overload
    def __mul__(self, formula: 整数クラス | int | 分数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __mul__(self, formula: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __mul__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __truediv__(self, formula: 整数クラス | int | 分数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __truediv__(self, formula: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __truediv__(self, formula: 式クラス) -> 式クラス: ...
    @overload
    def __mod__(self, formula: 整数クラス | int | 分数クラス) -> 整数クラス | 分数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, formula: float | 浮動小数クラス) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, formula: 式クラス) -> 式クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, formula: 式クラス) -> 式クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __pow__(
        self,
        formula: 整数クラス | int | 浮動小数クラス | float | 分数クラス | 式クラス,
    ) -> 式クラス: ...
    @overload
    def __radd__(self, formula: int | 整数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __radd__(self, formula: float) -> 浮動小数クラス: ...
    @overload
    def __rsub__(self, formula: int | 整数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __rsub__(self, formula: float) -> 浮動小数クラス: ...
    @overload
    def __rmul__(self, formula: int | 整数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __rmul__(self, formula: float) -> 浮動小数クラス: ...
    @overload
    def __rtruediv__(self, formula: int | 整数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __rtruediv__(self, formula: float) -> 浮動小数クラス: ...
    @overload
    def __rmod__(self, formula: int | 整数クラス) -> 整数クラス | 分数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rmod__(self, formula: float) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    def __rfloordiv__(self, formula: float | int) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            formula: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rpow__(self, formula: int | 整数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __rpow__(self, formula: float) -> 式クラス: ...
    @property
    def 抽象構文木(self) -> 抽象構文木クラス: ...
    def キャストできるか(self, タイプ: type[浮動小数クラス] | type[整数クラス]) -> bool: ...
    @property
    def 次数(self) -> int:
        """
            式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        ...
    @property
    def 分母(self) -> int: ...
    def 表示(self) -> 分数クラス: ...
    def 取得する_係数s(self, フォーカス変数: str, 整数を制限すべきか: bool = False) -> list[分数クラス]: ...
    @property
    def は整数か(self) -> bool | None: ...
    @property
    def 数(self) -> int | NativeFraction: ...
    @property
    def 分子(self) -> int: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数(self) -> set[str]: ...

express_fraction = tuple[
    int | float | NativeFraction,
    int | float | NativeFraction,
]

##### ./wip/designed/inequation.py #####

class 不等式クラス:
    def __init__(
        self,
        proof: 証明クラス,
        express: str | express_inequation,
        is_strict_mode: bool = False,
    ) -> None: ...
    def __invert__(self) -> symbol_condition: ...
    def __and__(self, other: bool | symbol_condition) -> symbol_condition:
        """
        論理和の中置演算子

        Args:
            other : 演算対象
        """
        ...
    def __or__(self, other: bool | symbol_condition) -> symbol_condition: ...
    def __eq__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ne__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __le__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __gt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ge__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lshift__(self, other: SymbolCondition) -> 数理命題クラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャストできるか(self, タイプ: type_from_term_inequation) -> 数理的ブールクラス: ...
    def キャスト可能なタイプ(self) -> list[type_from_term_inequation]: ...
    @property
    def 次数(self) -> int:
        """
            式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        ...
    def 表示する(
        self,
        状態: Literal[
            "row", "factorized", "factorized_and_split"
        ] = "factorized_and_split",
    ) -> 不等式クラス: ...
    @property
    def 評価された(self) -> 不等式クラス | 数理的ブールクラス: ...
    def 因数分解する(self) -> 不等式クラス: ...
    @property
    def 式(self) -> tuple[式クラス, 式クラス]: ...
    def 作成する_図(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順の軸順: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    def プロットする(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順の軸順: bool = True,
        タイトル: str = "",
    ) -> SymbolCondition: ...
    @property
    def 解かれた(self) -> 不等式クラス | 数理的ブールクラス | 複合条件クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def テキスト_因数分解後(self) -> str: ...
    @property
    def 変数(self) -> set[str]: ...

class 不等式_v1クラス(不等式クラス):
    def __init__(
        self,
        proof: 証明クラス,
        express: str | express_inequation,
        is_strict_mode: bool = False,
    ) -> None: ...
    def __sub__(self, formula: 不等式_v1クラス) -> 複合条件_v2クラス | 複合条件_v1クラス | 方程式クラス: ...
    def __eq__(self, formula: 不等式_v1クラス) -> bool: ...
    def __ne__(self, formula: 不等式_v1クラス) -> bool: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def 可能か_整数セットの取得(self, セット制限: int = 1000, エラーを発生させるべきか: bool = False) -> bool: ...
    def キャスト可能な型(self) -> list[type_from_term_inequation]: ...
    def 取得する_整数セット(self, セット制限: int = 1000) -> set[int]: ...
    @property
    def 範囲(self) -> markdown_str: ...

class 不等式_v2クラス(不等式クラス):
    def __init__(
        self,
        proof: 証明クラス,
        express: str | express_inequation,
        is_strict_mode: bool = False,
    ) -> None: ...
    def __sub__(self, formula: 不等式_v1クラス) -> 複合条件_v2クラス | 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャスト可能な型(self) -> list[type_from_term_inequation]: ...

express_inequation = tuple[term, term]
literal_eq = Literal["="]

##### ./wip/designed/integer.py #####

class 整数クラス:
    """
    整数を扱うクラスです。
    """

    def __init__(self, proof: 証明クラス, express: int) -> None: ...
    def __ne__(self, other: term_) -> 数理的ブールクラス | 非等号クラス:
        """
        不等式関係を評価します。
        """
        ...
    def __lt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス:
        """
        より小さい関係を評価します。
        """
        ...
    def __le__(self, other: term_) -> 数理的ブールクラス | 不等式クラス:
        """
        以下の関係を評価します。
        """
        ...
    def __gt__(self, other: term_) -> 数理的ブールクラス | 不等式クラス:
        """
        より大きい関係を評価します。
        """
        ...
    def __ge__(self, other: term_) -> 数理的ブールクラス | 不等式クラス:
        """
        以上の関係を評価します。
        """
        ...
    def __format__(self, __format_spec: str) -> str:
        """
        フォーマットされたテキストを返します。
        """
        ...
    @overload
    def __rshift__(self, type: type[浮動小数クラス]) -> 浮動小数クラス: ...
    @overload
    def __rshift__(self, type: type[式クラス]) -> 式クラス: ...
    @overload
    def __rshift__(self, type: type[分数クラス]) -> 分数クラス: ...
    @overload
    def __rshift__(self, type: type[整数クラス]) -> 整数クラス: ...
    @overload
    def __add__(self, other: 整数クラス | int) -> 整数クラス: ...
    @overload
    def __add__(self, other: 分数クラス) -> 分数クラス: ...
    @overload
    def __add__(self, other: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __add__(self, other: 式クラス) -> 式クラス: ...
    @overload
    def __sub__(self, other: 整数クラス | int) -> 整数クラス: ...
    @overload
    def __sub__(self, other: 分数クラス) -> 分数クラス: ...
    @overload
    def __sub__(self, other: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __sub__(self, other: 式クラス) -> 式クラス: ...
    def __neg__(self) -> 整数クラス: ...
    @overload
    def __mul__(self, other: 整数クラス | int) -> 整数クラス: ...
    @overload
    def __mul__(self, other: 分数クラス) -> 分数クラス: ...
    @overload
    def __mul__(self, other: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __mul__(self, other: 式クラス) -> 式クラス: ...
    @overload
    def __truediv__(self, other: 整数クラス | int | 分数クラス) -> 分数クラス | 整数クラス: ...
    @overload
    def __truediv__(self, other: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @overload
    def __truediv__(self, other: 式クラス) -> 式クラス: ...
    @overload
    def __mod__(self, other: 整数クラス | int) -> 整数クラス:
        """
        [%] の中置演算子

        引数:
            other: 整数クラス | int
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, other: 分数クラス) -> 整数クラス | 分数クラス:
        """
        [%] の中置演算子

        引数:
            other: 分数クラス
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, other: float | 浮動小数クラス) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            other: 浮動小数クラス
        結果:
            式クラス
        """
        ...
    @overload
    def __mod__(self, other: 式クラス) -> 式クラス:
        """
        [%] の中置演算子

        引数:
            other: 式クラス
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, other: 整数クラス | int | 浮動小数クラス | float | 分数クラス) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __floordiv__(self, other: 式クラス) -> 式クラス:
        """
        [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __pow__(self, other: 整数クラス | int) -> 整数クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __pow__(self, other: 式クラス | float | 浮動小数クラス | 分数クラス) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __radd__(self, other: int | 整数クラス) -> 整数クラス:
        """
        [+] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __radd__(self, other: float) -> 浮動小数クラス:
        """
        [+] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rsub__(self, other: int | 整数クラス) -> 整数クラス:
        """
        [-] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rsub__(self, other: float) -> 浮動小数クラス:
        """
        [-] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rmul__(self, other: int | 整数クラス) -> 整数クラス:
        """
        [*] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rmul__(self, other: float) -> 浮動小数クラス:
        """
        [*] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rtruediv__(self, other: int | 整数クラス) -> 整数クラス | 分数クラス:
        """
        [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rtruediv__(self, other: float) -> 浮動小数クラス:
        """
        [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rpow__(self, other: int | 整数クラス) -> 整数クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rpow__(self, other: float) -> 式クラス:
        """
        [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rmod__(self, other: int | 整数クラス) -> 整数クラス:
        """
        [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @overload
    def __rmod__(self, other: float) -> 浮動小数クラス:
        """
        [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __rfloordiv__(self, other: float | int) -> 整数クラス:
        """
        [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    def __eq__(self, term: term_) -> 数理的ブールクラス | 方程式クラス: ...
    def キャスト可能か(self, 型: type[浮動小数クラス] | type[分数クラス]) -> bool:
        """
        キャストが可能かどうかを返します。
        """
        ...
    @property
    def 次数(self) -> int:
        """
            式の最大の次数を返します。

        注意:

        整数多項式以外は、正しい結果を返さない。

        例）(x**2 + (1/x)**5) -> 5
        """
        ...
    def 表示する(self) -> 整数クラス:
        """
        表示します。
        """
        ...
    @property
    def 約数の個数(self) -> 整数クラス:
        """
        約数の個数を返します。
        """
        ...
    @property
    def 約数の和(self) -> 整数クラス:
        """
        約数の和を返します。
        """
        ...
    @property
    def 約数s(self) -> list[int]:
        """
        約数のリストを返します。
        """
        ...
    def 係数sを取得する(self, フォーカス変数: str, 整数を制限すべきか: bool = False) -> list[整数クラス]:
        """
        係数を返します。
        """
        ...
    def 取得する_べき乗された剰余(
        self,
        べき乗: int,
        mod: int,
        _範囲: tuple[int, int] = (1, 5),
        セクションタイトル: str = "乗数の剰余",
        セクションID: str = "取得する_べき乗された剰余",
    ) -> 式クラス: ...
    def 取得する_自身までの素数のリスト(self) -> list[int]:
        """
        自身までの素数のリストを返します。
        """
        ...
    def 取得する_積に分解したペア(
        self, 一意性: Literal["combination", "order"] = "order", マイナスを含むか: bool = False
    ) -> set[tuple[int, int]]:
        """
        積に分解したペアを返します。
        """
        ...
    @property
    def 整数であるか(self) -> bool | None:
        """
        整数であるかどうかを返します。
        """
        ...
    @property
    def 素数であるか(self) -> bool:
        """
        素数であるかどうかを返します。
        """
        ...
    @overload
    def 互いに素であるか(
        self,
        その他: 整数クラス | int,
        互いに素なペア: list[tuple[int | 整数クラス | 式クラス, int | 整数クラス | 式クラス]] = [],
    ) -> bool:
        """
        互いに素であるかどうかを返します。
        """
        ...

    @overload
    def 互いに素なペア(
        self,
        その他: 式クラス,
        互いに素なペア: list[tuple[int | 整数クラス | 式クラス, int | 整数クラス | 式クラス]] = [],
    ) -> bool | None:
        """
        互いに素であるかどうかを返します。
        """
        ...
    def 互いに素であるか(
        self,
        その他: 整数クラス | int | 式クラス,
        互いに素なペア: list[tuple[int | 整数クラス | 式クラス, int | 整数クラス | 式クラス]] = [],
    ) -> bool | None: ...
    @property
    def 数(self) -> int:
        """
        数値表現を返します。
        """
        ...
    def 素因数分解する(self) -> dict[int, int]:
        """
        素因数分解を行い、結果を返します。
        """
        ...
    @staticmethod
    def 証明する_素数が無限に存在すること(
        証明: 証明クラス,
        セクションタイトル: str = "素数が無限にある証明",
        セクションID: str = "証明する_素数が無限に存在すること",
    ) -> 整数クラス:
        """
        素数が無限に存在することを証明します。
        """
        ...
    @staticmethod
    def 証明する_有理平方根を持つならば整数(
        証明: 証明クラス,
        根: str = "m",
        分子: str = "q",
        分母: str = "l",
        セクションタイトル: str = "証明する_有理平方根を持つならば整数",
    ) -> bool:
        """
        「有理平方根を持つならば整数」ことを証明します。
        """
        ...
    @property
    def テキスト表現を返す(self) -> str:
        """
        テキスト表現を返します。
        """
        ...
    @property
    def 変数s(self) -> set[str]:
        """
        変数のセットを返します。
        """
        ...

##### ./wip/designed/integer_utils.py #####

class 整数便利ツール:
    @staticmethod
    @overload
    def 演算する_左(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: int | 整数クラス,
    ) -> 整数クラス: ...
    @staticmethod
    @overload
    def 演算する_左(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: float,
    ) -> 浮動小数クラス: ...
    @staticmethod
    @overload
    def 演算する_右(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: 整数クラス | int,
    ) -> 整数クラス: ...
    @staticmethod
    @overload
    def 演算する_右(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: 分数クラス,
    ) -> 分数クラス: ...
    @staticmethod
    @overload
    def 演算する_右(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: 浮動小数クラス | float,
    ) -> 浮動小数クラス: ...
    @staticmethod
    @overload
    def 演算する_右(
        証明: 証明クラス,
        整数: 整数クラス,
        演算子: Callable[[variables, str, str | int | float], str],
        その他: 式クラス,
    ) -> 式クラス: ...
    @staticmethod
    @overload
    def 除算し切り捨てる(
        証明: 証明クラス,
        整数: 整数クラス,
        その他: 整数クラス | int | 浮動小数クラス | float | 分数クラス,
    ) -> 整数クラス:
        """
            [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 除算し切り捨てる(証明: 証明クラス, 整数: 整数クラス, その他: 式クラス) -> 式クラス:
        """
            [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    def 取得する_べき乗された剰余(
        証明: 証明クラス,
        整数: 整数クラス,
        べき乗: int,
        mod: int,
        _範囲: tuple[int, int] = (1, 5),
        セクションタイトル: str = "乗数の剰余",
        セクションID: str = "取得する_べき乗された剰余",
    ) -> 式クラス: ...
    @staticmethod
    def 取得する_積のペア(
        証明: 証明クラス,
        整数: 整数クラス,
        一意性: Literal["combination", "order"] = "order",
        形式: bool = False,
    ) -> set[tuple[int, int]]: ...
    @staticmethod
    @overload
    def 互いに素なペア(
        証明: 証明クラス,
        整数: 整数クラス,
        その他: 整数クラス | int,
        互いに素なペア: List[
            tuple[
                int | 整数クラス | 式クラス,
                int | 整数クラス | 式クラス,
            ]
        ] = [],
    ) -> bool: ...
    @staticmethod
    @overload
    def 互いに素なペア(
        証明: 証明クラス,
        整数: 整数クラス,
        その他: 式クラス,
        互いに素なペア: List[
            tuple[
                int | 整数クラス | 式クラス,
                int | 整数クラス | 式クラス,
            ]
        ] = [],
    ) -> bool | None: ...
    @staticmethod
    @overload
    def 取得する_剰余(証明: 証明クラス, 整数: 整数クラス, その他: 整数クラス | int) -> 整数クラス: ...
    @staticmethod
    @overload
    def 取得する_剰余(証明: 証明クラス, 整数: 整数クラス, その他: 分数クラス) -> 整数クラス | 分数クラス: ...
    @staticmethod
    @overload
    def 取得する_剰余(証明: 証明クラス, 整数: 整数クラス, その他: float | 浮動小数クラス) -> 浮動小数クラス: ...
    @staticmethod
    @overload
    def 取得する_剰余(証明: 証明クラス, 整数: 整数クラス, その他: 式クラス) -> 式クラス: ...
    @staticmethod
    @overload
    def べき乗を計算する(証明: 証明クラス, 整数: 整数クラス, その他: 整数クラス | int) -> 整数クラス:
        """
            [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def べき乗を計算する(
        証明: 証明クラス,
        整数: 整数クラス,
        その他: 式クラス | float | 浮動小数クラス | 分数クラス,
    ) -> 式クラス:
        """
            [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    def 証明する_素数が無限に存在すること(
        証明: 証明クラス,
        セクションタイトル: str = "素数が無限に存在することの証明",
        セクションID: str = "証明する_素数が無限に存在すること",
    ) -> type["整数便利ツール"]: ...
    @staticmethod
    def 証明する_有理平方根を持つならば整数(
        証明: 証明クラス,
        根: str = "m",
        分子: str = "q",
        分母: str = "l",
        セクションタイトル: str = "証明する_有理平方根を持つならば整数",
    ) -> bool: ...
    @staticmethod
    def 除算し切り捨てる_右_(証明: 証明クラス, 整数: 整数クラス, その他: float | int) -> 整数クラス:
        """
            [//] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 剰余_右_(証明: 証明クラス, 整数: 整数クラス, その他: int | 整数クラス) -> 整数クラス:
        """
            [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 剰余_右_(証明: 証明クラス, 整数: 整数クラス, その他: float) -> 浮動小数クラス:
        """
            [%] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def べき乗_右_(証明: 証明クラス, 整数: 整数クラス, その他: int | 整数クラス) -> 整数クラス:
        """
            [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def べき乗_右_(証明: 証明クラス, 整数: 整数クラス, その他: float) -> 式クラス:
        """
            [**] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 除算_右_(証明: 証明クラス, 整数: 整数クラス, その他: int | 整数クラス) -> 整数クラス | 分数クラス:
        """
            [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 除算_右_(証明: 証明クラス, 整数: 整数クラス, その他: float) -> 浮動小数クラス:
        """
            [/] の中置演算子

        引数:
            other: 式
        結果:
            式クラス
        """
        ...
    @staticmethod
    @overload
    def 除算する(
        証明: 証明クラス,
        整数: 整数クラス,
        その他: 整数クラス | int | 分数クラス,
    ) -> 分数クラス | 整数クラス: ...
    @staticmethod
    @overload
    def 除算する(証明: 証明クラス, 整数: 整数クラス, その他: 浮動小数クラス | float) -> 浮動小数クラス: ...
    @staticmethod
    @overload
    def 除算する(証明: 証明クラス, 整数: 整数クラス, その他: 式クラス) -> 式クラス: ...

##### ./wip/designed/intersect.py #####

class 交差集合クラス:
    def __init__(self, proof: 証明クラス, element: set[str]) -> None: ...
    def 表示する(self) -> 交差集合クラス: ...

##### ./wip/designed/markdown_contents.py #####

class マークダウンコンテンツクラス:
    def __init__(self, contents: list[str]) -> None: ...
    def 表示する(self, インデントの深さ: int = 0) -> マークダウンコンテンツクラス: ...

##### ./wip/designed/math_conditional.py #####

class 数理命題クラス(命題クラス):
    def __init__(
        self,
        sufficient_condition: SymbolCondition,
        necessary_condition: SymbolCondition,
        sufficient_condition_bool: bool = True,
        necessary_condition_bool: bool = True,
    ) -> None: ...
    def __format__(self, __format_spec: str) -> str: ...
    @property
    def 対偶(self) -> 数理命題クラス: ...
    @property
    def 逆(self) -> 数理命題クラス: ...
    @property
    def 裏(self) -> 数理命題クラス: ...
    @property
    def 反対(self) -> 数理命題クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def テキスト_必要条件(self) -> str: ...
    @property
    def テキスト_十分条件(self) -> str: ...

##### ./wip/designed/math_markdown_sign.py #####

class 数学マークダウン記号クラス:
    """
    数学記号のまとめ
    """

    @staticmethod
    def 注釈() -> str: ...
    @staticmethod
    def なぜなら() -> str: ...
    @staticmethod
    def 省略記号() -> str: ...
    @staticmethod
    def 全角スペース() -> str: ...
    @staticmethod
    def 半角プラススペース() -> str: ...
    @staticmethod
    def 半角スペース() -> str: ...
    @staticmethod
    def 従って() -> str: ...

##### ./wip/designed/proof.py #####

class 証明クラス:
    """
    証明における説明、変数を管理するクラス
    """

    def __init__(self) -> None:
        """
        コンストラクタ
        """
        ...
    @overload
    def 追加する_説明(self, コンテンツ: explain, セクション: str = "") -> 証明クラス: ...
    @overload
    def 追加する_説明(
        self,
        コンテンツ: relation_content,
        セクション: str = "",
        順接か: bool = False,
        補足: str = "",
        補足のタイプ: Literal["because", "annotate", "plain"] = "because",
    ) -> 証明クラス: ...
    def 表示する_説明(self, セクション: str = "") -> 証明クラス: ...
    def 取得する_セクション(self, タイトル: str) -> セクションクラス:
        """
            関数の説明タイトル

        関数についての説明文

        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明.

        Returns:
            戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Yields:
            戻り値の型: 戻り値についての説明

        Examples:

            関数の使い方について記載

            >>> print_test ("test", "message")
                test message

        Note:
            注意事項などを記載
        """
        ...
    @overload
    def 取得する_変数(self, 変数: list[str] | set[str]) -> list[式クラス]: ...
    @overload
    def 取得する_変数(self, 変数: str) -> 式クラス: ...
    def 挿入する_セクション(
        self,
        セクション: セクションクラス | str,
        親セクション: str | セクションクラス | None = None,
    ) -> 証明クラス: ...
    def 変数か(self, 式: Union[式クラス, str]) -> bool: ...
    def 作成する_セクション(self, タイトル: str, ID: str) -> セクションクラス: ...
    def 作成する_一時的なセクションID(self, ベースID: str) -> str: ...
    def 作成する_一時的な変数(self) -> 式クラス: ...
    @overload
    def 作成する_変数(
        self,
        変数s: str,
        変数の種類s: variable_type_optional | variable_types_optional = {},
    ) -> 式クラス: ...
    @overload
    def 作成する_変数(
        self,
        変数s: variables_list,
        変数の種類s: variable_type_optional | variable_types_optional = {},
    ) -> formulas: ...
    def 作成する_変数s(
        self,
        変数s: str,
        変数の種類s: variable_type_optional | variable_types_optional = {},
    ) -> formulas: ...
    def 登録する_変数s(
        self, 変数s: list[str], 変数の種類s: variable_types_optional = {}
    ) -> 証明クラス: ...
    @property
    def セクションタイトルs(self) -> list[str]:
        """
            _summary_

        Returns:
            list[str]: _description_
        """
        ...
    def 更新する_変数s(self, 変数s: variables) -> 証明クラス: ...
    @property
    def 変数s(self) -> variables: ...

variables_list = list[str]
variables_set = set[str]
formulas = list[式クラス]

##### ./wip/designed/py_utils.py #####


class pythonユーティリティクラス:
    @staticmethod
    def 表示する_安全に(内容s: str | Markdown | Math) -> None: ...
    @overload
    @staticmethod
    def 取得する_すべての組み合わせ(選択肢s: list[list[int]]) -> list[list[int]]: ...
    @overload
    @staticmethod
    def 取得する_すべての組み合わせ(選択肢s: list[list[float]]) -> list[list[float]]: ...
    @overload
    @staticmethod
    def 取得する_すべての組み合わせ(選択肢s: list[list[str]]) -> list[list[str]]: ...
    @staticmethod
    def 生成する_ランダムな名前(n: int, 小文字のみ: bool) -> str: ...
    @staticmethod
    def 浮動小数点数か(文字列: str) -> bool: ...
    @staticmethod
    def 分数か(文字列: str) -> bool: ...
    @staticmethod
    def 整数か(文字列: str) -> bool: ...
    @staticmethod
    def 数か(文字列: str) -> bool: ...
    @staticmethod
    def 変換する_範囲を辞書からタプルに(
        プロット範囲: plotRanges, アルファベット順: bool = True, 変数s: set[str] = set()
    ) -> plotRange_2d: ...
    @staticmethod
    def 変換する_範囲をシングルからツインに(プロット範囲: plotRange) -> plotRange_2d: ...
    @staticmethod
    def 変換する_範囲を2Dプロット範囲に(
        プロット範囲: None | plotRanges | plotRange | plotRange_2d,
        アルファベット順: bool = True,
        変数s: set[str] = set(),
    ) -> plotRange_2d: ...

##### ./wip/designed/relation_content.py #####

class 関係コンテンツクラス:
    def __init__(
        self,
        content: relation_content,
        is_therefore_sign: bool = False,
        appendix: str = "",
        appendix_type: Literal["because", "annotate", "plain"] = "because",
    ) -> None: ...
    @property
    def 順接記号を継承(self) -> bool: ...
    @property
    def 内容(self) -> relation_content: ...
    def 表示する(
        self,
        インデントの深さ: int = 0,
        前の内容: 関係コンテンツクラス | None = None,
        省略モード: Literal["off", "on", "auto"] = "auto",
    ) -> 関係コンテンツクラス: ...

##### ./wip/designed/section.py #####

class セクションクラス:
    """
    セクション

    引数:
        id(str): id
    """

    def __init__(self, proof: 証明クラス, title: str, id: str) -> None: ...
    def __getitem__(self, index: int) -> explain: ...
    @overload
    def __setitem__(self, index: int, value: セクションクラス) -> セクションクラス: ...
    @overload
    def __setitem__(self, index: int, value: 関係コンテンツクラス) -> 関係コンテンツクラス: ...
    def __iter__(self) -> Generator[explain, None, None]: ...
    @overload
    def 追加する(self, コンテンツ: explain, 順接か: bool = False) -> セクションクラス: ...
    @overload
    def 追加する(
        self,
        コンテンツ: relation_content,
        順接か: bool = False,
        補足: str = "",
        補足のタイプ: Literal["because", "annotate", "plain"] = "because",
    ) -> セクションクラス: ...
    def 表示する(self, インデントの深さ: int = 0) -> セクションクラス: ...
    def 挿入する_セクション(self, セクション: セクションクラス | str) -> セクションクラス: ...
    def 作成する_サブセクション(
        self, タイトル: str, ID: str, インデックス: int | None = None
    ) -> セクションクラス: ...

##### ./wip/designed/symbol_condition_utils.py #####

class 数理的条件ユーティリティクラス:
    """
    条件クラス

    Attributes:
        variables (set[str]): 条件中で用いられる変数
        text (str): 条件中で用いられる変数
    """

    @staticmethod
    def 論理和(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> symbol_condition:
        """
            論理和の中置演算子

        Args:
            other : 演算対象
        """
        ...
    @staticmethod
    def 表示する(証明: 証明クラス, 条件: SymbolCondition) -> type["数理的条件ユーティリティクラス"]: ...
    @staticmethod
    def 等価(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def フォーマット(条件: SymbolCondition) -> str: ...
    @staticmethod
    def 以上(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def 大なり(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def 反転する(証明: 証明クラス, 条件_左: SymbolCondition) -> symbol_condition: ...
    @staticmethod
    def 以下(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def 左シフト(条件_左: SymbolCondition, 条件_右: SymbolCondition) -> 数理命題クラス: ...
    @staticmethod
    def 小なり(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def 作成する_図(
        証明: 証明クラス,
        条件: SymbolCondition,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット軸順: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    @staticmethod
    def 非等価(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> 数理的ブールクラス: ...
    @staticmethod
    def 論理積(
        証明: 証明クラス,
        条件_左: SymbolCondition,
        条件_右: bool | symbol_condition,
    ) -> symbol_condition: ...
    @staticmethod
    def プロットする(
        証明: 証明クラス,
        条件: SymbolCondition,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット軸順: bool = True,
        タイトル: str = "",
    ) -> type["数理的条件ユーティリティクラス"]: ...

##### ./wip/designed/symbolic_bool.py #####

class 数理的ブールクラス:
    def __init__(self, proof: 証明クラス, bool: bool) -> None: ...
    def __lt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __le__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __gt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ge__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __lshift__(self, other: SymbolCondition) -> 数理命題クラス: ...
    def __bool__(self) -> bool: ...
    def __invert__(self) -> 数理的ブールクラス: ...
    def __eq__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ne__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    @overload
    def __and__(self, other: bool | 数理的ブールクラス) -> 数理的ブールクラス: ...
    @overload
    def __and__(self, other: symbol_range) -> symbol_condition: ...
    @overload
    def __or__(self, other: bool | 数理的ブールクラス) -> 数理的ブールクラス: ...
    @overload
    def __or__(self, other: symbol_range) -> symbol_condition: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[定義式クラス]) -> 定義式クラス: ...
    @overload
    def __rshift__(self, type: type[説明式クラス]) -> 説明式クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def キャスト可能(self, 型: type_from_term_inequation) -> 数理的ブールクラス: ...
    def キャスト可能な型(self) -> list[type_from_term_inequation]: ...
    def 表示する(self) -> 数理的ブールクラス: ...
    def 作成する_図(
        self,
        プロット範囲s: plotRange | plotRanges | plotRange_2d | None,
        アルファベット軸順: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    @property
    def ネイティブブール(self) -> bool: ...
    def プロットする(
        self,
        プロット範囲s: plotRange | plotRanges | plotRange_2d | None,
        アルファベット軸順: bool = True,
        タイトル: str = "",
    ) -> SymbolCondition: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]: ...

##### ./wip/designed/table.py #####

class テーブルクラス:
    def __init__(self, data: table_data) -> None: ...
    def 追加する_列(
        self, 列名: str | int | float, ボディ: list[str | int | float]
    ) -> テーブルクラス: ...
    def 追加する_行(self) -> テーブルクラス: ...
    @property
    def データ(self) -> table_data: ...
    def 表示する(self) -> テーブルクラス: ...
    def 撤廃する_表示制限(self, 方向: Literal["row", "column"]) -> テーブルクラス: ...
    def 設定する_インデックス(self, 列名: str) -> テーブルクラス: ...

##### ./wip/designed/term_utils.py #####

class 項ユーティリティクラス:
    @staticmethod
    def 確認する_整数か(証明: 証明クラス, 項: Term) -> bool | None: ...
    @staticmethod
    def 表示する(証明: 証明クラス, 項: Term) -> type["項ユーティリティクラス"]: ...
    @staticmethod
    def 評価する_等価(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 方程式クラス: ...
    @staticmethod
    def 評価する_以上(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 不等式クラス: ...
    @staticmethod
    def 評価する_大なり(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 不等式クラス: ...
    @staticmethod
    def 評価する_以下(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 不等式クラス: ...
    @staticmethod
    def 評価する_小なり(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 不等式クラス: ...
    @staticmethod
    def 評価する_非等価(証明: 証明クラス, 項_左: Term, 項_右: term_) -> 数理的ブールクラス | 非等号クラス: ...
    @staticmethod
    def 取得する_次数(証明: 証明クラス, 項: Term) -> int:
        """
            式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        ...
    @staticmethod
    def 取得する_フォーマットテキスト(項: Term) -> str: ...
    @staticmethod
    def 取得する_文字列テキスト(項: Term) -> str: ...

##### ./wip/designed/text_conditional.py #####

class 文章命題クラス(命題クラス):
    def __init__(
        self,
        sufficient_condition: str,
        necessary_condition: str,
        sufficient_condition_bool: bool = True,
        necessary_condition_bool: bool = True,
    ) -> None: ...
    @property
    def 対偶(self) -> 文章命題クラス: ...
    @property
    def 逆(self) -> 文章命題クラス: ...
    @property
    def 裏(self) -> 文章命題クラス: ...
    @property
    def 反対(self) -> 文章命題クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def テキスト_対偶(self) -> str: ...
    @property
    def テキスト_逆(self) -> str: ...
    @property
    def テキスト_裏(self) -> str: ...
    @property
    def 必要条件のテキスト(self) -> str: ...
    @property
    def テキスト_反対(self) -> str: ...
    @property
    def 十分条件のテキスト(self) -> str: ...

express_term = tuple[term, term]

##### ./wip/designed/unequation.py #####

class 非等号クラス:
    def __init__(self, proof: 証明クラス, equation: str | express_term) -> None: ...
    def __invert__(self) -> symbol_condition: ...
    def __and__(self, other: bool | symbol_condition) -> symbol_condition:
        """
        論理和の中置演算子

        Args:
            other : 演算対象
        """
        ...
    def __or__(self, other: bool | symbol_condition) -> symbol_condition: ...
    def __eq__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ne__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __lt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __le__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __gt__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __ge__(self, other: bool | symbol_condition) -> 数理的ブールクラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __lshift__(self, other: SymbolCondition) -> 数理命題クラス: ...
    @overload
    def __rshift__(self, type: type[数理的ブールクラス]) -> 数理的ブールクラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v1クラス]) -> 不等式_v1クラス: ...
    @overload
    def __rshift__(self, type: type[不等式_v2クラス]) -> 不等式_v2クラス: ...
    @overload
    def __rshift__(self, type: type[不等式クラス]) -> 不等式クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v1クラス]) -> 複合条件_v1クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件_v2クラス]) -> 複合条件_v2クラス: ...
    @overload
    def __rshift__(self, type: type[複合条件クラス]) -> 複合条件クラス: ...
    @overload
    def __rshift__(self, type: type[方程式クラス]) -> 方程式クラス: ...
    @overload
    def __rshift__(self, type: type[非等号クラス]) -> 非等号クラス: ...
    def 型にキャスト可能か(self, 型: type_from_term_inequation) -> 数理的ブールクラス: ...
    def キャスト可能な型(self) -> list[type_from_term_inequation]: ...
    def 表示する(self, 生か: bool = True) -> 非等号クラス: ...
    @property
    def 評価済み(self) -> 非等号クラス | 数理的ブールクラス: ...
    def 因数分解する(self) -> 非等号クラス: ...
    @property
    def 式s(self) -> tuple[式クラス, 式クラス]: ...
    def 同一か(self) -> bool: ...
    def 作成する_図(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット軸順: bool = True,
        タイトル: str = "",
    ) -> 図形クラス: ...
    def プロットする(
        self,
        プロット範囲: plotRange | plotRanges | plotRange_2d | None,
        アルファベット順の軸の並び順: bool = True,
        タイトル: str = "",
    ) -> SymbolCondition: ...
    def 代入する(
        self,
        条件: dict[str, float] | dict[str, int] | dict[str, Term] | 方程式クラス | 方程式sクラス,
        辺: Literal["left", "right"] | None = None,
    ) -> 非等号クラス: ...
    @property
    def テキスト(self) -> str: ...
    @property
    def 表示用テキスト(self) -> str: ...
    @property
    def 入力用テキスト(self) -> str: ...
    @property
    def 変数s(self) -> set[str]:
        """
        式の変数
        """
        ...


##### ./wip/designed/utils.py #####

class 便利ツールクラス:
    @staticmethod
    def キャスト可能か(型: term_type, テキスト: str) -> bool: ...
    @staticmethod
    def キャストする(
        証明: 証明クラス, 型: term_type, テキスト: str
    ) -> 整数クラス | 浮動小数クラス | 分数クラス | 式クラス: ...
    @staticmethod
    def 表示する(内容s: str | Markdown) -> None: ...
    @staticmethod
    def 表示する_行式(証明: 証明クラス, 式: str) -> None:
        """
            式を評価せずに表示する
        要改修:
            ()が評価されて消えてしまう。
            x/xは評価されて1になってしまう。（変数宣言する必要あり）
        """
        ...
    @staticmethod
    @overload
    def ユークリッドの互除法(
        証明: 証明クラス, 項s: tuple[int, int], セクションタイトル: str
    ) -> tuple[int, int]: ...
    @staticmethod
    @overload
    def ユークリッドの互除法(
        証明: 証明クラス, 項s: tuple[str, str], セクションタイトル: str
    ) -> tuple[str, str]: ...
    @staticmethod
    def 取得する_素数(範囲: tuple[int, int]) -> list[int]: ...
    @staticmethod
    def 取得する_呼び出し元の行番号() -> int:
        """
            関数の呼び出し元の行番号を取得
        注意:
            !呼び出し元の上位行がすべて空の場合、常に1を返してしまうbugありTODO:修正!

        結果:
            呼び出し元の行
        """
        ...

##### ./wip/designed/variable_handling.py #####

class 変数ハンドラークラス:
    @staticmethod
    def 生成する_変数シンボル(
        既存の変数シンボル: dict[str, variable_symbol],
        変数s: list[str],
        変数の型s: variable_types_optional = {},
    ) -> dict[str, variable_symbol]: ...

##### ./wip/designed/vector.py #####

class ベクトルクラス:
    def __init__(self, proof: 証明クラス, elements: list[term_instance]) -> None: ...
    def __add__(self, other: ベクトルクラス) -> ベクトルクラス:
        """
        [+] の中置演算子

        引数:
            other: ベクトルクラス
        結果:
            ベクトルクラス
        """
        ...
    def __sub__(self, other: ベクトルクラス) -> ベクトルクラス:
        """
        [-] の中置演算子

        引数:
            other: ベクトルクラス
        結果:
            ベクトルクラス
        """
        ...
    def __neg__(self) -> ベクトルクラス: ...
    def __format__(self, __format_spec: str) -> str: ...
    def __getitem__(self, index: int) -> term_instance: ...
    def __iter__(self) -> Generator[term_instance, None, None]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: ベクトルクラス) -> bool: ...
    def 追加する(self, 要素: term_instance) -> ベクトルクラス: ...
    def 表示する(self) -> None: ...
    @property
    def 変数s(self) -> set[str]: ...

class ベクトル式クラス(ベクトルクラス):
    def __init__(self, proof: 証明クラス, elements: list[式クラス]) -> None: ...
    def __getitem__(self, index: int) -> 式クラス: ...
    def __iter__(self) -> Generator[term_instance, None, None]: ...
    def 追加する(self, 要素: 式クラス) -> ベクトル式クラス: ...

class 整数ペアクラス(ベクトルクラス):
    def __init__(
        self,
        proof: 証明クラス,
        pair: integer_pair_input,
        sum: integer_candidate_input | None = None,
        product: integer_candidate_input | None = None,
    ) -> None: ...
    def __getitem__(self, index: int) -> 式クラス | 整数クラス: ...
    @property
    def 要素s(self) -> integer_pair: ...
    @property
    def 積(self) -> integer_candidate: ...
    @property
    def 総和(self) -> integer_candidate: ...

class 自然数ペアクラス(整数ペアクラス):
    def __init__(
        self,
        proof: 証明クラス,
        pair: integer_pair_input,
        sum: integer_candidate_input | None = None,
        product: integer_candidate_input | None = None,
        gcd: integer_candidate_input | None = None,
        lcm: integer_candidate_input | None = None,
        relational_prime_pairs: list[
            tuple[integer_candidate_input, integer_candidate_input]
        ] = [],
    ) -> None: ...
    def 表示する_最大公約数履歴(self) -> 自然数ペアクラス: ...
    @property
    def 最大公約数(self) -> 自然数ペアクラス | integer_candidate: ...
    @property
    def 最大公約数の履歴(self) -> セクションクラス: ...
    @overload
    def 同定する_条件から(
        self,
        総和: int,
        最小公倍数: None,
        最大公約数: int,
        セクションタイトル: str = "同定する_条件から",
        セクションID: str = "同定する_条件から",
    ) -> ベクトル解sクラス: ...
    @overload
    def 同定する_条件から(
        self,
        総和: int,
        最小公倍数: int,
        最大公約数: None = None,
        セクションタイトル: str = "同定する_条件から",
        セクションID: str = "同定する_条件から",
    ) -> ベクトル解sクラス: ...
    @property
    def 最小公倍数(self) -> integer_candidate | None: ...
    @property
    def 積の関係式(self) -> 方程式クラス: ...
    @property
    def 総和の関係式(self) -> 方程式クラス | None: ...

##### ./wip/designed/vector_solutions.py #####

class ベクトル解sクラス:
    def __init__(
        self,
        proof: 証明クラス,
        equations: list[ベクトル方程式クラス] | list[解sクラス],
    ) -> None: ...
    def __getitem__(self, index: int) -> ベクトル方程式クラス: ...
    def __iter__(self) -> Generator[ベクトル方程式クラス, None, None]: ...
    def __format__(self, __format_spec: str) -> str: ...
    def 追加する(self, ベクトル方程式s: list[ベクトル方程式クラス] | ベクトル解sクラス) -> ベクトル解sクラス: ...
    def 追加する(self, ベクトル方程式: ベクトル方程式クラス) -> ベクトル解sクラス: ...
    @property
    def 方程式s(self) -> list[ベクトル方程式クラス]: ...

##### ./wip/designed/ven_diagram.py #####

class ベン図クラス:
    def __init__(self, data: list[vennData]) -> None: ...
    def 表示する(self): ...

##### ./wip/designed/ven_diagram_reservation.py #####

class ベン図登録クラス:
    def __init__(self, data: list[vennData]) -> None: ...
    def 表示する(self) -> ベン図登録クラス: ...

##### ./wip/designed/define_type.py #####

SymbolCondition = Union[方程式クラス, 不等式クラス, 非等号クラス, 複合条件クラス, 数理的ブールクラス]
Term = Union[式クラス, 浮動小数クラス, 整数クラス, 分数クラス]

class subtract_prime_result(TypedDict):
    term: 式クラス
    signInteger: Literal[1, -1]

class Modee(TypedDict):
    residual: int
    power: int

markdown_str = str
integer_candidate = Union[整数クラス, 式クラス]
integer_candidate_input = Union[int, integer_candidate]
integer_pair_input = tuple[integer_candidate_input, integer_candidate_input]
integer_pair = tuple[integer_candidate, integer_candidate]
condition_symbol = Literal["True", "False"]
equation_symbol_ = Literal["="]
inequality_relation = Literal["<", "<=", ">", ">="]
inequation_symbol = Literal["<", "<=", ">", ">="]
term_type = Union[type[整数クラス], type[浮動小数クラス], type[分数クラス], type[式クラス]]
table_data = dict[str, list[Union[str, int, float]]]
unequation_symbol = Literal["!="]
plotRange_ = tuple[
    tuple[Union[int, float], Union[int, float]],
    tuple[Union[int, float], Union[int, float]],
]
symbol_relation_type = Literal[
    operator_symbol,
    number_symbol,
    condition_symbol,
    equation_symbol_,
    inequation_symbol,
    unequation_symbol,
]
symbol_type = Literal[symbol_relation_type, "symbol", condition_symbol]
type_from_term_inequation = Union[
    type[数理的ブールクラス],
    type[不等式クラス],
    type[不等式_v1クラス],
    type[不等式_v2クラス],
    type[方程式クラス],
    type[非等号クラス],
    type[複合条件クラス],
    type[複合条件_v1クラス],
    type[複合条件_v2クラス],
]
# variables = dict[str, variable_symbol]
single_condition = Union[方程式クラス, 非等号クラス, 不等式クラス, 不等式_v1クラス, 不等式_v2クラス, 数理的ブールクラス]
symbol_range = Union[
    方程式クラス, 非等号クラス, 不等式クラス, 不等式_v1クラス, 不等式_v2クラス, 複合条件クラス, 複合条件_v1クラス, 複合条件_v2クラス
]
symbol_condition = Union[symbol_range, 数理的ブールクラス]

class squared_result(TypedDict):
    square: 式クラス
    correction_term: 式クラス

class add_and_subtract_products_equation(TypedDict):
    left_plus_term: 式クラス
    left_minus_term: 式クラス
    right_constant_term: Union[整数クラス, 分数クラス]

class euclidean_output_each_process(TypedDict):
    result: 自然数ペアクラス
    explain: セクションクラス

class euclidean_output(TypedDict):
    result: Union[自然数ペアクラス, integer_candidate]
    explain: セクションクラス

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


# Dependent type
variable_types_optional = dict[str, variable_type_optional]
explain = Union[セクションクラス, 関係コンテンツクラス, str, マークダウンコンテンツクラス, テーブルクラス, 図登録クラス, ベン図登録クラス]

class common_initialize_result(TypedDict):
    proof: 証明クラス
    ast: astElement
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

term_instance = Union[float, int, 整数クラス, 浮動小数クラス, 分数クラス, 式クラス]
conditions_float = dict[str, float]
conditions_int = dict[str, int]
conditions_str = dict[str, str]
conditions_term = dict[str, Term]
conditions_fraction = dict[str, NativeFraction]
conditions_native = Union[conditions_float, conditions_int, conditions_str]
term_ = Union[Term, float, int, NativeFraction]
term = Union[Term, str, float, int, NativeFraction]

class Position_only_x(TypedDict, total=True):
    x: Union[int, float, str]

class Position_only_y(TypedDict, total=True):
    y: Union[int, float, str]

class Position_only(Position_only_x, Position_only_y): ...

class Annotation(TypedDict, total=False):
    annotation: str

class Position(Position_only, Annotation): ...
class Position_x(Position_only_x, Annotation): ...

class Positions_only_x(TypedDict, total=True):
    x: Union[list[int], list[float], list[str]]

class Positions_only_y(TypedDict, total=True):
    y: list[Union[int, float, str]]

class Positions_only(Positions_only_x, Positions_only_y): ...

class Annotations(TypedDict, total=False):
    annotation: list[str]

class Positions_list(Positions_only, Annotations): ...
class Positions_list_x(Positions_only_x, Annotations): ...

class result_of_factorized_and_split(TypedDict):
    inequations: Union[tuple[tuple[不等式クラス, 不等式クラス], tuple[不等式クラス, 不等式クラス]], None]
    relation_index: Literal[0, 1, 2, 3]

relation_content = Union[
    symbol_condition, Term, 数理命題クラス, 解sクラス, ベクトル方程式クラス, ベクトル解sクラス, ベクトルクラス
]
