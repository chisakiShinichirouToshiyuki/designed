# pyright: reportUnusedImport=false
from __future__ import annotations
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING


class MarkdownContents:
    def __init__(self, contents: list[str]):
        pass

    def display(self, indent_depth: int = 0):
        pass



if TYPE_CHECKING:
    from . import DefineType  # type: ignore
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()