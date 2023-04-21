# pyright: reportUnusedImport=false
from __future__ import annotations
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING


class マークダウンコンテンツクラス:
    def __init__(self, contents: list[str]):
        pass

    def 表示する(self, 字下げ深さ: int = 0):
        pass



if TYPE_CHECKING:
    from . import 型定義クラス  # type: ignore
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()