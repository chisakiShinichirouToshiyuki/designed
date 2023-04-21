# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
# from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal
import re
from typing import overload
from typing import TYPE_CHECKING


class 方程式クラス:
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式:  Union[str , term_pair] ):
        pass



    # @abstractmethod
    def テキスト(self) -> str:  # type: ignore
        pass

    def __invert__(self) -> 型定義クラス.数理的コンディション:  # type: ignore
        """和

        Args:
            x (int): 1st argument
            y (int): 2nd argument

        Returns:
            int: 和 result

        Examples:
            >>> print(testfunc(2,5))
            7
        """
        pass

    def __and__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的コンディション:  # type: ignore
        """ 論理和の中置演算子

        Args:
            相手 : 演算対象

        """
        pass

    def __or__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的コンディション:  # type: ignore
        pass

    def __eq__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __ne__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __lt__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __le__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __gt__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __ge__(self, 相手:  Union[bool , 型定義クラス.数理的コンディション] ) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def __lshift__(self, 相手: 型定義クラス.数理的条件クラス) -> 型定義クラス.数理的命題クラス:  # type: ignore
        pass

    def 変換できるか(self, type: 型定義クラス.type_from_term_inequation) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        pass

    def 作成する_図形(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None] , アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.図形クラス:  # type: ignore
        pass

    def プロットする(self, 範囲ず_プロット:  Union[型定義クラス.プロット範囲 , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲_2次 , None] , アルファベット順: bool = True, タイトル: str = '') -> 型定義クラス.数理的条件クラス:  # type: ignore
        pass


    @property
    def 式ず(self) -> tuple[型定義クラス.式クラス, 型定義クラス.式クラス]:  # type: ignore
        pass

    @property
    def テキスト_表示用(self) -> str:  # type: ignore
        pass

    @property
    def テキスト_入力用(self) -> str:  # type: ignore
        pass

    @property
    def 次数(self) -> int:  # type: ignore
        """式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        pass

    @property
    def 変数ず(self) -> set[str]:  # type: ignore
        """式の変数
        """
        pass

    @property
    def 評価済(self) ->  Union[方程式クラス , 型定義クラス.数理的真偽クラス] :  # type: ignore
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    def 不定方程式を解く_d1_v2(self, パラメータ変数: str = 'k_', 走査範囲: tuple[int, int] = (-5, 5), 章タイトル: str = '１次２変数の不定方程式の解', 章ID: str = '不定方程式を解く_d1_v2') -> 型定義クラス.ベクトル方程式クラス:  # type: ignore
        pass

    def 不定方程式を解く_d1_v2_分解型(self, 章タイトル: str = '１次２変数の不定方程式(分解型)の解', 章ID: str = '不定方程式を解く_d1_v2_分解型') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        pass

    def 不定方程式を解く_d2_v2_分解型(self, 自然数かい: bool = False, 章タイトル: str = '２次２変数の不定方程式(分解型)の解', 章ID: str = '不定方程式を解く_d2_v2_分解型') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        pass

    def 不定方程式を解く_差の2乗型(self, 方程式: 型定義クラス.add_and_subtract_products_equation,  自然数かい: bool = False, 章タイトル: str = '２乗差の不定方程式の解', 章ID: str = '不定方程式を解く_差の2乗型') -> 型定義クラス.ベクトル解ずクラス:  # type: ignore
        pass

    def 不定方程式を解く_対称型(self, 変数の大きさの順: list[str] = [], 順序の厳密性: bool = False, 章タイトル: str = '対称式の不定方程式の解', 章ID: str = '不定方程式を解く_対称型') ->  Union[型定義クラス.ベクトル解ずクラス , None] :  # type: ignore
        """対称不定方程式を解く

        注意
        ----------
        変数の大小関係の引数に柔軟に対応する拡張が必要かも。現実装は、対応範囲が狭い。
        解が自然数に限る

        Parameters
        ----------
        証明
        方程式
            解くべき自然数不定方程式。右辺が整数である必要がある。
        変数の大きさの順:  
            変数の大小関係
        順序の厳密性
            大小関係が厳密か、等号を含むか

        Returns
        -------
        解ず: 
            不定方程式の解のセット
        """
        pass

    def 解く_両辺の差が急速に開く方程式(self, 走査範囲: tuple[int, int] = (0, 10), 章タイトル: str = '急速に差が開く等式の解法', 章ID: str = '解く_両辺の差が急速に開く方程式'):
        pass

    def 代入する(self, コンディションず:  Union[辞書_有限小数 , 辞書_整数 , 辞書_項 , 方程式クラス , 型定義クラス.方程式ずクラス] , side:  Union[左右 , None]  = None) -> 方程式クラス:  # type: ignore
        pass

    def 不定方程式を解の範囲を取得する(self, 変数の大きさの順: list[str], 順序の厳密性: bool = False,  章タイトル: str = '不定方程式の解の範囲', 章ID: str = '不定方程式を解の範囲を取得する') -> list[型定義クラス.不等式クラス]:  # type: ignore
        pass

    def 定義式かい(self) -> bool:  # type: ignore
        pass

    def 表示する(self, 素: bool = True):
        pass

    def 解く(self, ターゲット変数: str) -> list[型定義クラス.式クラス]:  # type: ignore
        pass

    def 恒等式かい(self) -> bool:  # type: ignore
        pass

    def 因数分解する(self) -> 方程式クラス:  # type: ignore
        pass

    def 取得する_1次2変数の特殊解(self, 走査範囲: tuple[int, int]) ->  Union[辞書_整数 , None] :  # type: ignore
        pass

    def __add__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __sub__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __neg__(self) -> 型定義クラス.分数クラス:  # type: ignore
        pass

    def __mul__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[*] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __truediv__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[/] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __pow__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __radd__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[+] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __rsub__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[-] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __rmul__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[*] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __rtruediv__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[/] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __rpow__(self, 方程式か項:  Union[型定義クラス.方程式クラス , 型定義クラス.項クラス , int , float , 型定義クラス.NativeFraction] ) -> 型定義クラス.方程式クラス:  # type: ignore
        """[**] の中置演算子 

        引数:
            式: 式
        結果: 
            式クラス
        """
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[型定義クラス.数理的真偽クラス]) -> 型定義クラス.数理的真偽クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式_v1クラス]) -> 型定義クラス.不等式_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式_v2クラス]) -> 型定義クラス.不等式_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.不等式クラス]) -> 型定義クラス.不等式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v1クラス]) -> 型定義クラス.複合条件_v1クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件_v2クラス]) -> 型定義クラス.複合条件_v2クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.複合条件クラス]) -> 型定義クラス.複合条件クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[定義式クラス]) -> 定義式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[説明式クラス]) -> 説明式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.方程式クラス]) -> 型定義クラス.方程式クラス:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[型定義クラス.非等式クラス]) -> 型定義クラス.非等式クラス:  # type: ignore
        ...

    def __rshift__(self, type:  Union[型定義クラス.type_from_term_inequation , 説明式クラス , 定義式クラス] ) ->  Union[型定義クラス.数理的コンディション , 説明式クラス , 定義式クラス] :  # type: ignore
        pass

    def 変換可能な型(self) -> list[型定義クラス.type_from_term_inequation]:  # type: ignore
        pass

class 方程式_2dクラス(方程式クラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式:  Union[str , term_pair] , main_variable: str = ''):
        pass


    @property
    def 解と係数の関係_積(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @property
    def 解と係数の関係_和(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @property
    def 判別式(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @property
    def a(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @property
    def b(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

    @property
    def c(self) -> 型定義クラス.式クラス:  # type: ignore
        pass

class 説明式クラス(方程式クラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式:  Union[str , formula_term_pair] ):
        pass
        # assert self.式ず[0].テキスト in list(self._証明.変数ず.keys())


class 定義式クラス(説明式クラス):
    def __init__(self, 証明: 型定義クラス.証明クラス, 方程式:  Union[str , formula_term_pair] ):
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
    term_pair = tuple[型定義クラス.項, 型定義クラス.項]
    formula_term_pair = tuple[型定義クラス.式クラス, 型定義クラス.項]
    辞書_有限小数 = dict[str, float]
    辞書_整数 = dict[str, int]
    辞書_項 = dict[str, 型定義クラス.項クラス]
    左右 = Literal['left', 'right']
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()
