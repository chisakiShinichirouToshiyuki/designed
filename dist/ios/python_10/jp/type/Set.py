# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
import re
from typing import TYPE_CHECKING


class Set:  # TODO FiniteSet対応
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: express_str | express_str_set | express_int_set | express_float_set = set()):
        pass


    @property
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def native_set(self) -> set[int]:  # type: ignore
        pass

    def 表示する(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
    express_str = str
    express_str_set = set[str]
    express_int_set = set[int]
    express_float_set = set[float]
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
