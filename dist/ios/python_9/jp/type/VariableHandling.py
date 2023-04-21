# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import TYPE_CHECKING


class VariableHandling:
    @staticmethod
    def create_variables_symbol(existed_variables: dict[str, 型定義クラス.variable_symbol], 変数ず: list[str], 変数タイプ: 型定義クラス.変数タイプずオプション = {}) -> dict[str, 型定義クラス.variable_symbol]:  # type: ignore
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
