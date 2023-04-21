# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING
from typing import cast
from typing import Generator
from typing import TYPE_CHECKING
from typing import overload


class ベクトルクラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, 要素ず: list[型定義クラス.項_インスタンス]) -> None:  # type: ignore
        pass


    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    @property
    def latex(self) -> str:  # type: ignore
        pass

    def 表示する(self) -> None:  # type: ignore
        pass

    def 追加する(self, 要素: 型定義クラス.項_インスタンス):
        pass

    def __add__(self, 相手: ベクトルクラス) -> ベクトルクラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            相手: ベクトルクラス
        結果: 
            ベクトルクラス
        """
        pass

    def __sub__(self, 相手: ベクトルクラス) -> ベクトルクラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            相手: ベクトルクラス
        結果: 
            ベクトルクラス
        """
        pass

    def __neg__(self) -> ベクトルクラス:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __getitem__(self, index: int)-> 型定義クラス.項_インスタンス:  # type: ignore
        pass

    def __iter__(self)-> Generator[型定義クラス.項_インスタンス, None, None]:  # type: ignore
        pass

    def __len__(self) -> int:  # type: ignore
        pass

    def __eq__(self, 相手: ベクトルクラス) -> bool:  # type: ignore
        pass

class 整数ペアクラス(ベクトルクラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, pair: 型定義クラス.整数ペア_インプット, 和: 型定義クラス.整数候補_インプット | None = None, 積: 型定義クラス.整数候補_インプット | None = None):
        pass


    def 要素ず(self):
        pass

    @property
    def 和(self) -> 型定義クラス.整数候補:  # type: ignore
        pass

    @property
    def 積(self) -> 型定義クラス.整数候補:  # type: ignore
        pass

    def __getitem__(self, index: int) -> 型定義クラス.式クラス | 型定義クラス.整数クラス:  # type: ignore
        pass

class 自然数ペアクラス(整数ペアクラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, pair: 型定義クラス.整数ペア_インプット,  和: 型定義クラス.整数候補_インプット | None = None, 積: 型定義クラス.整数候補_インプット | None = None, 最大公約数: 型定義クラス.整数候補_インプット | None = None, 最小公倍数: 型定義クラス.整数候補_インプット | None = None, 互いに素なペア: list[tuple[型定義クラス.整数候補_インプット, 型定義クラス.整数候補_インプット]] = []):
        pass


    @property
    def 最大公約数(self) -> 自然数ペアクラス | 型定義クラス.整数候補:  # type: ignore
        pass

    @property
    def 最大公約数の履歴(self) -> 型定義クラス.章クラス:  # type: ignore
        pass

    @property
    def 最小公倍数(self) -> 型定義クラス.整数候補 | None:  # type: ignore
        pass

    @property
    def 積の関係式(self) -> 型定義クラス.方程式クラス:  # type: ignore
        pass

    @property
    def 和の関係式(self) -> 型定義クラス.方程式クラス | None:  # type: ignore
        pass

    def 表示する_最大公約数の履歴(self):
        pass

    @overload
    def 同定する_条件より(self, 和: int, 最小公倍数: None, 最大公約数: int,  章タイトル: str = '自然数ペアの決定', 章ID: str = '同定する_条件より') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        ...

    @overload
    def 同定する_条件より(self, 和: int, 最小公倍数: int, 最大公約数: None = None, 章タイトル: str = '自然数ペアの決定', 章ID: str = '同定する_条件より') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        ...

    def 同定する_条件より(self, 和: int, 最小公倍数: int | None = None, 最大公約数: int | None = None, 章タイトル: str = '自然数ペアの決定', 章ID: str = '同定する_条件より') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
