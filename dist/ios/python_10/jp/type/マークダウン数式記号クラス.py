# pyright: reportUnusedImport=false
from typing import TYPE_CHECKING

class マークダウン数式記号クラス():
    """数学記号のまとめ
    """

    @staticmethod
    def annotation() -> str:  # type: ignore
        pass

    @staticmethod
    def because() -> str:  # type: ignore
        pass

    @staticmethod
    def ellipsis() -> str:  # type: ignore
        pass

    @staticmethod
    def full_space() -> str:  # type: ignore
        pass

    @staticmethod
    def half_plus_space() -> str:  # type: ignore
        pass

    @staticmethod
    def half_space() -> str:  # type: ignore
        pass

    @staticmethod
    def therefore() -> str:  # type: ignore
        pass

if TYPE_CHECKING:
    from . import 型定義クラス  # type: ignore
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()

