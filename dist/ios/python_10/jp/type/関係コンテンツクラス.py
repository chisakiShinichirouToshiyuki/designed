# pyright: reportUnusedImport=false
from __future__ import annotations
from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal


class 関係コンテンツクラス:
    def __init__(self, コンテンツ: 型定義クラス.関係コンテンツ, 順接かい: bool = False, 補足: str = '', 補足タイプ: Literal['because', 'annotate', 'plain'] = 'because'):
        pass


    @property
    def コンテンツ(self) -> 型定義クラス.関係コンテンツ:  # type: ignore
        pass

    @property
    def 順接記号の継承(self) -> bool:  # type: ignore
        pass


    @property
    def 表示する(self, 字下げ深さ: int = 0, 前のコンテンツ: 関係コンテンツクラス | None = None, 省略モード: Literal['off', 'on', 'auto'] = 'auto'):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
