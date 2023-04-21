# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import TYPE_CHECKING


class Intersect:
    def __init__(self, proof: DefineType.Proof, element: set[str]):
        pass

    def display(self):
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
