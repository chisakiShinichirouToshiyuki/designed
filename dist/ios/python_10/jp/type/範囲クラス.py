# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
import math
import re
from collections.abc import Callable
from typing import TYPE_CHECKING


class 範囲クラス():
    def __init__(self, 証明: 型定義クラス.証明クラス, 表現形: str):
        pass

    # Private 属性

    # Getter
    @property
    def 抽象木(self) -> 型定義クラス.抽象木クラス:  # type: ignore
        pass

    @property
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    def 変換する_集合(self, 変数: str) -> 型定義クラス.Set:  # type: ignore
        pass

    def 取得できるか_整数の集合(self, 抽象木:  型定義クラス.抽象木要素 | None = None, 走査範囲: int = 1000, エラーを出すべきか: bool = False) -> bool:  # type: ignore
        pass

    def 表示する(self):
        pass

    def 取得する_整数集合(self, 抽象木:  型定義クラス.抽象木要素 | None = None, 走査範囲: int = 1000) -> set[int]:  # type: ignore
        pass

    def __or__(self, 式:  型定義クラス.範囲クラス) -> 型定義クラス.Set | 型定義クラス.範囲クラス:  # type: ignore
        pass

    def __and__(self, 式:  型定義クラス.範囲クラス) -> 型定義クラス.Set | 型定義クラス.範囲クラス:  # type: ignore
        pass

    def __sub__(self, 式:  型定義クラス.範囲クラス) -> 型定義クラス.Set | 型定義クラス.範囲クラス:  # type: ignore
        pass

    def __eq__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __ne__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __lt__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __le__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __gt__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __ge__(self, 式:  型定義クラス.範囲クラス) -> bool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> 型定義クラス.markdown_str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
