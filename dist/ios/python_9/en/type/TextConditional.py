# pyright: reportUnusedImport=false
from __future__ import annotations
import colorama
from .Conditional import Conditional
from typing import TYPE_CHECKING


class TextConditional(Conditional):
    def __init__(self, sufficient_condition: str, necessary_condition: str, sufficient_condition_bool: bool = True, necessary_condition_bool: bool = True):
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
    def text_converse(self) -> str:  # type: ignore
        pass

    @property
    def text_inverse(self) -> str:  # type: ignore
        pass

    @property
    def text_contrapositive(self) -> str:  # type: ignore
        pass

    @property
    def text_opposition(self) -> str:  # type: ignore
        pass

    @property
    def converse(self) -> TextConditional:  # type: ignore
        pass

    @property
    def inverse(self) -> TextConditional:  # type: ignore
        pass

    @property
    def contrapositive(self) -> TextConditional:  # type: ignore
        pass

    @property
    def opposition(self) -> TextConditional:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
    express_term = tuple[DefineType.term, DefineType.term]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()