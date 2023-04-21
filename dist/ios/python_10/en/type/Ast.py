# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import cast
from typing import Literal
from typing import TypedDict
from typing import TYPE_CHECKING


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


class Ast:
    """数式の抽象木

    数式の解析に使う
    """

    def __init__(self, proof: DefineType.Proof, express: str, assertee_function: list[DefineType.symbol_type] = [], variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}):
        pass


    # @property
    # def text_for_markdown(self)->str:  # type: ignore
    #     pass

    def assert_function(self, assert_function: list[DefineType.symbol_type], should_regressive_search: bool = False) -> Ast:  # type: ignore
        """数式の抽象木

        数式の解析に使う
        """
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    @property
    def text(self) -> str:  # type: ignore
        """数式の抽象木

        数式の解析に使う
        """
        pass

    @property
    def element(self) -> DefineType.astElement:  # type: ignore
        pass

    @property
    def element_not_evaluated(self) -> DefineType.astElement:  # type: ignore
        pass

    @property
    def evaluate(self) -> DefineType.astElement:  # type: ignore
        pass

    @property
    def factors(self) -> list[str]:  # type: ignore
        pass

    @property
    def ast_prettified_inequation_for_factorize(self) -> DefineType.astElement:  # type: ignore
        pass

    @staticmethod
    def get_plotable_condition_list(ast: DefineType.astElement, all_variables: DefineType.variables, conditions: list[DefineType.astElement] = []) -> list[DefineType.astElement]:  # type: ignore
        pass

    def get_end_leafs(self, ast: DefineType.astElement | None = None, leaf_type: list[DefineType.symbol_relation_type] = [], leafs: list[DefineType.astElement] = []) -> list[DefineType.astElement]:  # type: ignore
        pass

    def get_power_term(self, ast: DefineType.astElement | None = None) -> list[str]:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
