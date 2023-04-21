# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import TYPE_CHECKING


class Intersect:
    def __init__(self, 証明: 型定義クラス.証明クラス, 要素: set[str]):
        pass

    def 表示する(self):
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
