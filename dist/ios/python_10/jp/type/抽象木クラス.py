# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import cast
from typing import Literal
from typing import TypedDict
from typing import TYPE_CHECKING


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


class 抽象木クラス:
    """数式の抽象木

    数式の解析に使う
    """

    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: str, チェック対象の演算子: list[型定義クラス.symbol_type] = [], 変数タイプ: 型定義クラス.変数タイプオプション | 型定義クラス.変数タイプずオプション = {}):
        pass


    # @property
    # def text_for_markdown(self)->str:  # type: ignore
    #     pass

    def チェックする_演算子(self, チェックする_演算子: list[型定義クラス.symbol_type], should_regressive_search: bool = False) -> 抽象木クラス:  # type: ignore
        """数式の抽象木

        数式の解析に使う
        """
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    @property
    def テキスト(self) -> str:  # type: ignore
        """数式の抽象木

        数式の解析に使う
        """
        pass

    @property
    def 要素(self) -> 型定義クラス.抽象木要素:  # type: ignore
        pass

    @property
    def 要素_未評価(self) -> 型定義クラス.抽象木要素:  # type: ignore
        pass

    @property
    def 評価済(self) -> 型定義クラス.抽象木要素:  # type: ignore
        pass

    @property
    def 因数ず(self) -> list[str]:  # type: ignore
        pass

    @property
    def 抽象木_因数分解向けに整形済(self) -> 型定義クラス.抽象木要素:  # type: ignore
        pass

    @staticmethod
    def 取得する_プロット可能なコンディションのリスト(抽象木: 型定義クラス.抽象木要素, 全変数: 型定義クラス.変数ず, コンディションず: list[型定義クラス.抽象木要素] = []) -> list[型定義クラス.抽象木要素]:  # type: ignore
        pass

    def 取得する_終端(self, 抽象木: 型定義クラス.抽象木要素 | None = None, leaf_type: list[型定義クラス.演算子] = [], leafs: list[型定義クラス.抽象木要素] = []) -> list[型定義クラス.抽象木要素]:  # type: ignore
        pass

    def 取得する_乗数項(self, 抽象木: 型定義クラス.抽象木要素 | None = None) -> list[str]:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
