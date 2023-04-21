# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
import re
from typing import TYPE_CHECKING


class Set:  # TODO FiniteSet対応
    def __init__(self, proof: DefineType.Proof, express:  Union[express_str , express_str_set , express_int_set , express_float_set]  = set()):
        pass


    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def native_set(self) -> set[int]:  # type: ignore
        pass

    def display(self):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
    express_str = str
    express_str_set = set[str]
    express_int_set = set[int]
    express_float_set = set[float]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
