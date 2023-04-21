# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from .PlotAdapter import AxBase
from typing import TYPE_CHECKING
from typing import Literal
from typing import Any


class 座標クラス(AxBase):
    def __init__(self, 図形: 型定義クラス.図形クラス, 座標: Any):
        pass


    def プロットする_式の曲線(self, 式:  Union[型定義クラス.式クラス , str , float , int , 型定義クラス.NativeFraction] , 変数: str, color: 型定義クラス.hsla = (220, 100, 50), label: str = '') -> 座標クラス:  # type: ignore
        pass

    def プロットする_散布式(self, data: list[型定義クラス.Position_x] | 型定義クラス.Positions_list_x, 式:  Union[型定義クラス.式クラス , str , float , int , 型定義クラス.NativeFraction] , 変数: str, color:  Union[型定義クラス.プロットカラー , 型定義クラス.hex_rgb]  = 'black', label: str = '') -> 座標クラス:  # type: ignore
        pass

    def プロットする_散布点(self, data: list[型定義クラス.Position] | 型定義クラス.Positions_list, color:  Union[型定義クラス.プロットカラー , 型定義クラス.hex_rgb] ) -> 座標クラス:  # type: ignore
        pass

    def プロットする_数理的コンディション(self, condition: 型定義クラス.数理的条件クラス, 軸ず: list[str] | None = None, color:  Union[型定義クラス.hsla , None]  = None) -> 座標クラス:  # type: ignore
        """
        """
        pass

    def 足す_グリッド(self) -> 座標クラス:  # type: ignore
        pass

    def 再設定する_範囲(self, _範囲: 型定義クラス.プロット範囲_2次) -> 座標クラス:  # type: ignore
        """グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        pass

    def 再設定する_タイトル(self, タイトル: str) -> 座標クラス:  # type: ignore
        """グラフ範囲の設定

        注意:
            再設定は、エリアの追加前にする必要がある。
        """
        pass

    def 再設定する_ラベル(self, ラベルず: tuple[str, str]) -> 座標クラス:  # type: ignore
        pass

    def 再設定する_プロット属性(self, 属性: Literal['dot_radius', 'line_width', 'z_oder'], 値:  Union[float , int] ) -> 座標クラス:  # type: ignore
        pass

    def 設定する_凡例(self) -> 座標クラス:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
