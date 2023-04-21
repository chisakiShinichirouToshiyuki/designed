# pyright: reportUnusedImport=false
from __future__ import annotations
from .Conditional import Conditional
from typing import TYPE_CHECKING


class MathConditional(Conditional):
    def __init__(self, sufficient_condition: DefineType.SymbolCondition, necessary_condition: DefineType.SymbolCondition, sufficient_condition_bool: bool = True, necessary_condition_bool: bool = True):
        pass


    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def text_necessary_condition(self) -> str:  # type: ignore
        pass

    @property
    def text_sufficient_condition(self) -> str:  # type: ignore
        pass

    @property
    def converse(self) -> MathConditional:  # type: ignore
        pass

    @property
    def inverse(self) -> MathConditional:  # type: ignore
        pass

    @property
    def contrapositive(self) -> MathConditional:  # type: ignore
        pass

    @property
    def opposition(self) -> MathConditional:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
