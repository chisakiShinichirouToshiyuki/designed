# pyright: reportUnusedImport=false
from __future__ import annotations
import colorama
from .命題クラス import 命題クラス
from typing import TYPE_CHECKING


class 文章命題クラス(命題クラス):
    def __init__(self, 十分条件: str, 必要条件: str, 十分条件の真偽: bool = True, 必要条件の真偽: bool = True):
        pass

    @property
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_必要条件(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_十分条件(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_裏(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_逆(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_対偶(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_反対(self) -> str:  # type: ignore
        pass

    @property
    def 裏(self) -> 文章命題クラス:  # type: ignore
        pass

    @property
    def 逆(self) -> 文章命題クラス:  # type: ignore
        pass

    @property
    def 対偶(self) -> 文章命題クラス:  # type: ignore
        pass

    @property
    def 反対(self) -> 文章命題クラス:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
    表現形_項 = tuple[型定義クラス.項, 型定義クラス.項]
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()