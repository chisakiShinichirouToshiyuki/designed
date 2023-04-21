# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
import math
import re
from collections.abc import Callable
from typing import TYPE_CHECKING


class Range():
    def __init__(self, proof: DefineType.Proof, express: str):
        pass

    # Private property

    # Getter
    @property
    def ast(self) -> DefineType.Ast:  # type: ignore
        pass

    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    def as_set(self, variable: str) -> DefineType.Set:  # type: ignore
        pass

    def can_get_set_integer(self, ast:  DefineType.astElement | None = None, set_limit: int = 1000, should_raise_error: bool = False) -> bool:  # type: ignore
        pass

    def display(self):
        pass

    def get_set_integer(self, ast:  DefineType.astElement | None = None, set_limit: int = 1000) -> set[int]:  # type: ignore
        pass

    def __or__(self, formula:  DefineType.Range) -> DefineType.Set | DefineType.Range:  # type: ignore
        pass

    def __and__(self, formula:  DefineType.Range) -> DefineType.Set | DefineType.Range:  # type: ignore
        pass

    def __sub__(self, formula:  DefineType.Range) -> DefineType.Set | DefineType.Range:  # type: ignore
        pass

    def __eq__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __ne__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __lt__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __le__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __gt__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __ge__(self, formula:  DefineType.Range) -> bool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> DefineType.markdown_str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
