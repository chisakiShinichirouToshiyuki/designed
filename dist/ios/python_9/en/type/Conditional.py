# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from abc import ABCMeta
from abc import abstractmethod
from IPython.display import Markdown  # type: ignore
from typing import Literal
from typing import TYPE_CHECKING

class Conditional(metaclass=ABCMeta):
    def __init__(self, sufficient_condition: str, necessary_condition: str, sufficient_condition_bool: bool = True, necessary_condition_bool: bool = True, ):
        pass



    @abstractmethod
    def text(self) -> str:  # type: ignore
        pass


    @abstractmethod
    def text_necessary_condition(self) -> str:  # type: ignore
        pass


    @abstractmethod
    def text_sufficient_condition(self) -> str:  # type: ignore
        pass

    @property
    def text_converse(self) -> str:  # type: ignore
        pass

    @property
    def text_inverse(self) -> str:  # type: ignore
        pass

    @property
    def text_contrapositive(self) -> str:  # type: ignore
        pass

    @property
    def text_opposition(self) -> str:  # type: ignore
        pass


    @abstractmethod
    def converse(self) -> Conditional:  # type: ignore
        pass


    @abstractmethod
    def inverse(self) -> Conditional:  # type: ignore
        pass


    @abstractmethod
    def contrapositive(self) -> Conditional:  # type: ignore
        pass


    @abstractmethod
    def opposition(self) -> Conditional:  # type: ignore
        pass

    def analyze_strategy(self) -> Conditional:  # type: ignore
        pass

    def add_suffix(self, segment_index: Literal[0, 1], opinion: bool) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType  # type: ignore
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()

