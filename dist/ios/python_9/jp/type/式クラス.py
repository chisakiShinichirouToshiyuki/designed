# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
import random
from typing import overload
from typing import TYPE_CHECKING
from copy import deepcopy


default_condition: 型定義クラス.condition = {
    'times': 0,
    'mod': [0]
}


class 式クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, テキスト:  Union[str , float , int] , 変数タイプ:  Union[型定義クラス.変数タイプオプション , 型定義クラス.変数タイプずオプション]  = {}):
        pass


    @property
    def 抽象木(self) -> 抽象木クラス.抽象木クラス:  # type: ignore
        pass

    @property
    def 平方完成(self) -> 型定義クラス.squared_result:  # type: ignore
        pass

    @property
    def 次数(self) -> int:  # type: ignore
        pass

    @property
    def 因数分解の要素(self) -> list[式クラス]:  # type: ignore
        """因数分解の因数(次数なし)
        """
        pass

    @property
    def 整数かい(self) ->  Union[bool , None] :  # type: ignore
        pass

    @property
    def テキスト(self) -> str:  # type: ignore
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        pass

    def 変換できるか(self, type: type[型定義クラス.整数クラス] | type[型定義クラス.有限小数クラス] | type[型定義クラス.分数クラス]) -> bool:  # type: ignore
        pass

    def チェックする_対称式(self) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def 表示する(self):
        pass

    def 微分する(self, ターゲット変数: str) -> 式クラス:  # type: ignore
        pass

    def 展開する(self) -> 式クラス:  # type: ignore
        pass

    def 因数分解する(self) -> 式クラス:  # type: ignore
        pass

    def 代入する_不安定版(self, subsitutee: tuple[str, 式クラス]) -> 式クラス:  # type: ignore
        pass

    def 取得する_係数ず(self, ターゲット変数: str, 制限するか_整数の範囲: bool = False) -> list[式クラス]:  # type: ignore
        pass

    def 取得する_因数(self) -> list[式クラス]:  # type: ignore
        pass

    def 同定する_条件より(self, 約数の個数: int, range: tuple[int, int], 章タイトル: str = '整数の特定', 章ID: str = '同定する_条件より') -> 型定義クラス.ベクトルクラス:  # type: ignore
        pass

    def 積分する(self) -> 式クラス:  # type: ignore
        pass

    def 整数かい_ラフ版(self, rough_search: bool = False, only_positive: bool = True) ->  Union[bool , None] :  # type: ignore
        pass

    def 特定の倍数か(self, times: int, expected_mod: list[int], condition: 型定義クラス.condition = default_condition, 章タイトル: str = 'proof_specific_times') -> bool:  # type: ignore
        pass

    def 互いに素かい(self, 相手:  Union[型定義クラス.整数クラス , int , 式クラス] , 互いに素なペア: list[tuple[ Union[int , 型定義クラス.整数クラス , 式クラス] ,  Union[int , 型定義クラス.整数クラス , 式クラス] ]] = []) ->  Union[bool , None] :  # type: ignore
        pass

    def 作成する_図形(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None]  = None, タイトル: str = '') -> 型定義クラス.図形クラス:  # type: ignore
        pass

    def 変形する_1変数化(self, ターゲット_変数: str):
        pass

    def ラフチェックする_単調増加性(self, points: list[int] = list(range(1, 100, 20)), is_in_Natural: bool = True) ->  Union[bool , None] :  # type: ignore
        pass

    def 解く(self, focus_term: str = '') -> list[式クラス]:  # type: ignore
        pass

    def 代入する(self, コンディションず:  Union[型定義クラス.conditions_float , 型定義クラス.conditions_int , 型定義クラス.conditions_str , 型定義クラス.conditions_term , 型定義クラス.方程式クラス , 型定義クラス.方程式ずクラス] ) -> 式クラス:  # type: ignore
        pass

    def proof_powers_modularity(self, mod: int, 章タイトル: str = '乗数の剰余', 章ID: str = 'proof_powers_modularity'):
        pass

    def プロットする(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None]  = None, タイトル: str = '', color: 型定義クラス.hsla = (220, 100, 50), label: str = '') -> 式クラス:  # type: ignore
        pass

    def __lt__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __le__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __gt__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __ge__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.不等式クラス] :  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    def __add__(self, 相手:   Union[float , int]  | 型定義クラス.整数クラス |  Union[型定義クラス.有限小数クラス , 型定義クラス.分数クラス]  | 式クラス) -> 式クラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            相手: 演算子の左側の式
        結果: 
            式クラス
        """
        pass

    def __sub__(self, 相手:  Union[式クラス , float , int , 型定義クラス.分数クラス , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __neg__(self) -> 式クラス:  # type: ignore
        pass

    def __mul__(self, 相手:  Union[式クラス , float , int , 型定義クラス.分数クラス , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[*] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __truediv__(self, 相手:  Union[式クラス , float , int , 型定義クラス.分数クラス , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[/] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __pow__(self, 相手:  Union[式クラス , float , int , 型定義クラス.分数クラス , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __mod__(self, 相手:  Union[式クラス , float , int , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[%] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __floordiv__(self, 相手:  Union[式クラス , float , int , 型定義クラス.整数クラス , 型定義クラス.有限小数クラス] ) -> 式クラス:  # type: ignore
        """[//] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __radd__(self, 相手:  Union[float , int] ) -> 式クラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rsub__(self, 相手:  Union[float , int] ) -> 式クラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rmul__(self, 相手:  Union[float , int] ) -> 式クラス:  # type: ignore
        """[*] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rtruediv__(self, 相手:  Union[float , int] ) -> 式クラス:  # type: ignore
        """[/] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rpow__(self, 相手:  Union[float , int] ) -> 式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rmod__(self, 相手:   Union[float , int] ) -> 式クラス:  # type: ignore
        """[%] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    def __rfloordiv__(self, 相手:   Union[float , int] ) -> 式クラス:  # type: ignore
        """[//] の中置演算子 

        引数:
            相手: 式
        結果: 
            式クラス
        """
        pass

    @overload
    def __eq__(self, 相手: str) -> str:  # type: ignore
        ...

    @overload
    def __eq__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.方程式クラス] :  # type: ignore
        ...

    def __eq__(self, 相手:  Union[型定義クラス.term_ , str] ) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.方程式クラス]  | str:  # type: ignore
        pass

    @overload
    def __ne__(self, 相手: str) -> str:  # type: ignore
        ...

    @overload
    def __ne__(self, 相手: 型定義クラス.term_) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.非等式クラス] :  # type: ignore
        ...

    def __ne__(self, 相手:  Union[型定義クラス.term_ , str] ) ->  Union[型定義クラス.数理的真偽クラス , 型定義クラス.非等式クラス]  | str:  # type: ignore
        pass

    def check_operator(self, check_operator: list[型定義クラス.symbol_type]) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.整数クラス]) -> 型定義クラス.整数クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.有限小数クラス]) -> 型定義クラス.有限小数クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.分数クラス]) -> 型定義クラス.分数クラス:  # type: ignore
        ...

    def __rshift__(self, type: type[型定義クラス.整数クラス] | type[型定義クラス.有限小数クラス] | type[型定義クラス.分数クラス]) ->  Union[型定義クラス.有限小数クラス , 型定義クラス.整数クラス , 型定義クラス.分数クラス] :  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
