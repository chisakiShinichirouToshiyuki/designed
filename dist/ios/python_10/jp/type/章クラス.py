# pyright: reportUnusedImport=false
from __future__ import annotations
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal
from typing import Generator
from typing import overload


class 章クラス:
    """セクション

    引数:
        id(str): id

    """

    def __init__(self, 証明: 型定義クラス.証明クラス, タイトル: str, id: str):
        pass


    def 作成する_下位の章(self, タイトル: str, id: str, index: int | None = None) -> 章クラス:  # type: ignore
        pass

    def __getitem__(self, index: int)-> 型定義クラス.説明:  # type: ignore
        pass

    @overload
    def __setitem__(self, index: int, 値: 章クラス) -> 章クラス:  # type: ignore
        ...

    @overload
    def __setitem__(self, index: int, 値: 型定義クラス.関係コンテンツクラス) -> 型定義クラス.関係コンテンツクラス:  # type: ignore
        ...

    def __setitem__(self, index: int, 値: 章クラス | 型定義クラス.関係コンテンツクラス) -> 章クラス | 型定義クラス.関係コンテンツクラス:  # type: ignore
        pass

    def __iter__(self) -> Generator[型定義クラス.説明, None, None]:  # type: ignore
        pass

    @overload
    def 追加する(self, コンテンツ: 型定義クラス.説明, 順接かい: bool = False) -> 章クラス:  # type: ignore
        ...

    @overload
    def 追加する(self, コンテンツ: 型定義クラス.関係コンテンツ, 順接かい: bool = False, 補足: str = '', 補足タイプ: Literal['because', 'annotate', 'plain'] = 'because') -> 章クラス:  # type: ignore
        ...

    def 追加する(self, コンテンツ: 型定義クラス.説明 | 型定義クラス.関係コンテンツ, 順接かい: bool = False, 補足: str = '', 補足タイプ: Literal['because', 'annotate', 'plain'] = 'because') -> 章クラス:  # type: ignore
        pass

    def 挿入する_章(self, 章: 章クラス | str)->章クラス:  # type: ignore
        pass

    def 表示する(self, 字下げ深さ: int = 0) -> 章クラス:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
