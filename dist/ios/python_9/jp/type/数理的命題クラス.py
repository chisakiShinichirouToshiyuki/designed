# pyright: reportUnusedImport=false
from __future__ import annotations
from .命題クラス import 命題クラス
from typing import TYPE_CHECKING


class 数理的命題クラス(命題クラス):
    def __init__(self, 十分条件: 型定義クラス.数理的条件クラス, 必要条件: 型定義クラス.数理的条件クラス, 十分条件の真偽: bool = True, 必要条件の真偽: bool = True):
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
    def 裏(self) -> 数理的命題クラス:  # type: ignore
        pass

    @property
    def 逆(self) -> 数理的命題クラス:  # type: ignore
        pass

    @property
    def 対偶(self) -> 数理的命題クラス:  # type: ignore
        pass

    @property
    def 反対(self) -> 数理的命題クラス:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
