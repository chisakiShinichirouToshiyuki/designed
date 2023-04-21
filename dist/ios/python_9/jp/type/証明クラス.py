# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from IPython.display import Markdown, Math  # type: ignore
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
import random


class 証明クラス:
    """証明における説明、変数を管理するクラス
    """


    def __init__(self):
        """コンストラクタ
        """
        pass

    @property
    def 変数ず(self) -> 型定義クラス.変数ず:  # type: ignore
        pass

    @property
    def 章タイトルず(self) -> list[str]:  # type: ignore
        """_summary_

        Returns:
            list[str]: _description_
        """
        pass

    def 取得する_章(self, タイトル: str) -> 型定義クラス.章クラス:  # type: ignore
        """関数の説明タイトル

        関数についての説明文

        Args:
            引数の名前 (引数の型): 引数の説明
            引数の名前 (:obj:`引数の型`, optional): 引数の説明.

        Returns:
            戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Yields:
            戻り値の型: 戻り値についての説明

        Examples:

            関数の使い方について記載

            >>> print_test ("test", "message")
                test message

        Note:
            注意事項などを記載

        """
        pass

    def 作成する_使い捨て変数(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    def 作成する_使い捨て章ID(self, 基本ID: str) -> str:  # type: ignore
        pass

    @overload
    def 取得する_変数(self, 変数: list[str] | set[str]) -> list[型定義クラス.式クラス]:  # type: ignore
        ...

    @overload
    def 取得する_変数(self, 変数: str) -> 型定義クラス.式クラス:  # type: ignore
        ...

    def 取得する_変数(self, 変数:  Union[str , 変数リスト , 変数セット] ) ->  Union[型定義クラス.式クラス , 式ず] :  # type: ignore
        pass

    def 更新する_変数ず(self, 変数ず: 型定義クラス.変数ず):
        pass

    @overload
    def 作成する_変数(self, 変数ず: str, 変数タイプ:  Union[型定義クラス.変数タイプオプション , 型定義クラス.変数タイプずオプション]  = {}) -> 型定義クラス.式クラス:  # type: ignore
        ...

    @overload
    def 作成する_変数(self, 変数ず: 変数リスト, 変数タイプ:  Union[型定義クラス.変数タイプオプション , 型定義クラス.変数タイプずオプション]  = {}) -> 式ず:  # type: ignore
        ...

    def 作成する_変数(self, 変数ず:  Union[str , 変数リスト] , 変数タイプ:  Union[型定義クラス.変数タイプオプション , 型定義クラス.変数タイプずオプション]  = {}) ->  Union[型定義クラス.式クラス , 式ず] :  # type: ignore
        pass

    def 作成する_変数ず(self, 変数ず: str, 変数タイプ:  Union[型定義クラス.変数タイプオプション , 型定義クラス.変数タイプずオプション]  = {}) -> 式ず:  # type: ignore
        pass

    def register_variables(self, 変数ず: list[str], 変数タイプ: 型定義クラス.変数タイプずオプション = {}):
        pass

    def 作成する_章(self, タイトル: str, id: str) -> 型定義クラス.章クラス:  # type: ignore
        pass

    @overload
    def 追加する_説明(self, コンテンツ: 型定義クラス.説明, 章: str = '') -> 証明クラス:  # type: ignore
        ...

    @overload
    def 追加する_説明(self, コンテンツ: 型定義クラス.関係コンテンツ, 章: str = '', 順接かい: bool = False, 補足: str = '', 補足タイプ: Literal['because', 'annotate', 'plain'] = 'because') -> 証明クラス:  # type: ignore
        ...

    def 追加する_説明(self,  コンテンツ:  Union[型定義クラス.説明 , 型定義クラス.関係コンテンツ] , 章: str = '', 順接かい: bool = False, 補足: str = '', 補足タイプ: Literal['because', 'annotate', 'plain'] = 'because') -> 証明クラス:  # type: ignore
        pass

    def 挿入する_章(self, 章:  Union[型定義クラス.章クラス , str] , 上位の章:  Union[str , 型定義クラス.章クラス , None]  = None) -> 証明クラス:  # type: ignore
        pass

    def 表示する_説明(self, 章: str = '') -> 証明クラス:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import 型定義クラス
    変数リスト = list[str]
    変数セット = set[str]
    式ず = list[型定義クラス.式クラス]
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
