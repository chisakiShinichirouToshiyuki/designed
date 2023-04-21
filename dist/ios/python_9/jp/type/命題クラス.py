# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
from IPython.display import Markdown  # type: ignore
from typing import Literal
from typing import TYPE_CHECKING

class 命題クラス(metaclass=ABCMeta):
    def __init__(self, 十分条件: str, 必要条件: str, 十分条件の真偽: bool = True, 必要条件の真偽: bool = True, ):
        pass



    @abstractmethod
    def テキスト(self) -> str:  # type: ignore
        pass


    @abstractmethod
    def テキスト_必要条件(self) -> str:  # type: ignore
        pass


    @abstractmethod
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


    @abstractmethod
    def 裏(self) -> 命題クラス:  # type: ignore
        pass


    @abstractmethod
    def 逆(self) -> 命題クラス:  # type: ignore
        pass


    @abstractmethod
    def 対偶(self) -> 命題クラス:  # type: ignore
        pass


    @abstractmethod
    def 反対(self) -> 命題クラス:  # type: ignore
        pass

    def 分析する_戦略(self) -> 命題クラス:  # type: ignore
        pass

    def 足す_接尾語(self, segment_index: Literal[0, 1], opinion: bool) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス  # type: ignore
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()

