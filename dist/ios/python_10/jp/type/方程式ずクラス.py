# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from IPython.display import Markdown, Math  # type: ignore
from typing import cast
from typing import TYPE_CHECKING
from IPython.display import Markdown  # type: ignore
from typing import Generator
# pyright: reportImportCycles=false


class 方程式ずクラス:
    # def __init__(self, 証明: 型定義クラス.証明クラス, 方程式ず:
    #         list[方程式クラス]
    #         | tuple[型定義クラス.ベクトルクラス,型定義クラス.ベクトルクラス]
    #         # | equation_list_row
    #         # | vector_tuple_row
    #     ):

    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式ず: 表現形_リスト | 表現形_タプル):
        pass


    @property
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    @property
    def 方程式ず(self) -> list[型定義クラス.方程式クラス]:  # type: ignore
        pass

    def 足す_方程式(self, 方程式ず: list[型定義クラス.方程式クラス]):
        pass

    def 追加する(self, 方程式: 型定義クラス.方程式クラス):
        pass

    def 解く(self, ターゲット_項ず: set[str] = set()) -> ベクトル方程式クラス | None:  # type: ignore
        pass

    def 表示する(self):
        pass

    def 削除する_変数(self, ターゲット_変数: str = '', 定義式: 型定義クラス.方程式クラス | None = None) -> 方程式ずクラス:  # type: ignore
        pass

    def __getitem__(self, index: int)-> 型定義クラス.方程式クラス:  # type: ignore
        pass

    def __iter__(self)-> Generator[型定義クラス.方程式クラス, None, None]:  # type: ignore
        pass

    def __len__(self) -> int:  # type: ignore
        pass

class 解ずクラス(方程式ずクラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式ず: list[型定義クラス.方程式クラス] | tuple[型定義クラス.ベクトルクラス, 型定義クラス.ベクトルクラス]):
        pass

    def 並び替え(self, 逆順にすべきか: bool = False) -> 解ずクラス:  # type: ignore
        pass

    def 表示する(self):
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __add__(self, 相手: 解ずクラス) -> 解ずクラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            相手: ベクトルクラス
        結果: 
            ベクトルクラス
        """
        pass

class ベクトル方程式クラス(方程式ずクラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式ず: list[型定義クラス.方程式クラス] | tuple[型定義クラス.ベクトルクラス, 型定義クラス.ベクトルクラス]):
        pass


    @property
    def ベクトル_左辺(self) -> 型定義クラス.ベクトルクラス:  # type: ignore
        pass

    @property
    def ベクトル_右辺(self) -> 型定義クラス.ベクトルクラス:  # type: ignore
        pass

    def 足す_方程式(self, 方程式ず: list[型定義クラス.方程式クラス]):
        pass

    def 追加する(self, 方程式: 型定義クラス.方程式クラス):
        pass

    def 並び替え(self, 逆順にすべきか: bool = False) -> ベクトル方程式クラス:  # type: ignore
        pass

    def 表示する(self):
        pass

    def __eq__(self, 相手: ベクトル方程式クラス) -> bool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
    表現形_リスト = list[型定義クラス.方程式クラス]
    表現形_タプル = tuple[型定義クラス.ベクトルクラス, 型定義クラス.ベクトルクラス]
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
