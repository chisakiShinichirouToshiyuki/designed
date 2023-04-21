# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import TYPE_CHECKING


class VariableHandling:
    @staticmethod
    def create_variables_symbol(existed_variables: dict[str, DefineType.variable_symbol], variables: list[str], variable_types: DefineType.variable_types_optional = {}) -> dict[str, DefineType.variable_symbol]:  # type: ignore
        pass



# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
