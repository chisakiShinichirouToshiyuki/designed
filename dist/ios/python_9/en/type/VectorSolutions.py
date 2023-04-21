# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import cast
from typing import TYPE_CHECKING
from typing import Generator


class VectorSolutions():
    def __init__(self, proof: DefineType.Proof, equations: list[DefineType.VectorEquation] | list[DefineType.Solutions]):
        pass


    @property
    def equations(self) -> list[DefineType.VectorEquation]:  # type: ignore
        pass

    def add(self, vector_equations: list[DefineType.VectorEquation] | VectorSolutions):
        pass

    def append(self, vector_equation: DefineType.VectorEquation):
        pass

    def __getitem__(self, index: int) -> DefineType.VectorEquation:  # type: ignore
        pass

    def __iter__(self)-> Generator[DefineType.VectorEquation, None, None]:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
