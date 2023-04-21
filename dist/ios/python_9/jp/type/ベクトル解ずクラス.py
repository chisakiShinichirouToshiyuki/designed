# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from typing import cast
from typing import TYPE_CHECKING
from typing import Generator


class ベクトル解ずクラス():
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式ず: list[型定義クラス.ベクトル方程式クラス] | list[型定義クラス.解ずクラス]):
        pass


    @property
    def 方程式ず(self) -> list[型定義クラス.ベクトル方程式クラス]:  # type: ignore
        pass

    def 足す(self, vector_equations: list[型定義クラス.ベクトル方程式クラス] | ベクトル解ずクラス):
        pass

    def 追加する(self, vector_equation: 型定義クラス.ベクトル方程式クラス):
        pass

    def __getitem__(self, index: int) -> 型定義クラス.ベクトル方程式クラス:  # type: ignore
        pass

    def __iter__(self)-> Generator[型定義クラス.ベクトル方程式クラス, None, None]:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
