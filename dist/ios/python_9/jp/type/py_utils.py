# pyright: reportUnusedImport=false
from __future__ import annotations 
from typing import Union 
from IPython.display import display, Markdown, Math  # type: ignore
from pprint import pprint
from typing import cast
from typing import overload
from typing import TYPE_CHECKING
import fractions
import random
import string
from typing import Union


plotRange = tuple[Union[int, float], Union[int, float]]

plotRanges = dict[str, plotRange]

plotRange_2d = tuple[plotRange, plotRange]
default_range: 型定義クラス.プロット範囲 = (-10, 10)


class Utils:

    @staticmethod
    def is_num(string: str) -> bool:  # type: ignore
        pass

    @staticmethod
    def is_float(string: str) -> bool:  # type: ignore
        pass

    @staticmethod
    def is_integer(string: str) -> bool:  # type: ignore
        pass

    @staticmethod
    def is_fraction(string: str) -> bool:  # type: ignore
        pass

    @staticmethod
    def get_random_name(n: int, lower_case: bool) -> str:  # type: ignore
        pass


    @staticmethod
    def get_all_combination(choices: list[list[int]]) -> list[list[int]]:  # type: ignore
        ...


    @staticmethod
    def get_all_combination(choices: list[list[float]]) -> list[list[float]]:  # type: ignore
        ...


    @staticmethod
    def get_all_combination(choices: list[list[str]]) -> list[list[str]]:  # type: ignore
        ...

    @staticmethod
    def get_all_combination(choices: list[list[int]] | list[list[float]] | list[list[str]]) -> list[list[int]] | list[list[float]] | list[list[str]]:  # type: ignore
        pass

    @staticmethod
    def translate_range_from_dict_to_tuple(plot_ranges: 型定義クラス.プロット範囲ず, alphabetic_axis_order: bool = True, variables: set[str] = set()) -> 型定義クラス.プロット範囲_2次:  # type: ignore
        pass

    @staticmethod
    def translate_range_from_single_to_twin(plot_range: 型定義クラス.プロット範囲) -> 型定義クラス.プロット範囲_2次:  # type: ignore
        pass

    @staticmethod
    def translate_range_to_plotRange_2d(plot_ranges:  Union[None , 型定義クラス.プロット範囲ず , 型定義クラス.プロット範囲 , 型定義クラス.プロット範囲_2次] , alphabetic_axis_order: bool = True, variables: set[str] = set()) -> 型定義クラス.プロット範囲_2次:  # type: ignore
        pass

    @staticmethod
    def display_safety(contents:  Union[str , Markdown , Math] ) -> None:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import 型定義クラス
else:
    from . import DefineType_mock
    型定義クラス = DefineType_mock.型定義クラス()