# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING
from typing import cast
from typing import Generator
from typing import TYPE_CHECKING
from typing import overload


class Vector:
    def __init__(self, proof: DefineType.Proof, elements: list[DefineType.term_instance]) -> None:  # type: ignore
        pass


    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    @property
    def latex(self) -> str:  # type: ignore
        pass

    def display(self) -> None:  # type: ignore
        pass

    def append(self, element: DefineType.term_instance):
        pass

    def __add__(self, other: Vector) -> Vector:  # type: ignore
        """[+] の中置演算子 

        引数:
            other: Vector
        結果: 
            Vector
        """
        pass

    def __sub__(self, other: Vector) -> Vector:  # type: ignore
        """[-] の中置演算子 

        引数:
            other: Vector
        結果: 
            Vector
        """
        pass

    def __neg__(self) -> Vector:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __getitem__(self, index: int)-> DefineType.term_instance:  # type: ignore
        pass

    def __iter__(self)-> Generator[DefineType.term_instance, None, None]:  # type: ignore
        pass

    def __len__(self) -> int:  # type: ignore
        pass

    def __eq__(self, other: Vector) -> bool:  # type: ignore
        pass

class IntegerPair(Vector):
    def __init__(self, proof: DefineType.Proof, pair: DefineType.integer_pair_input, sum:  Union[DefineType.integer_candidate_input , None]  = None, product:  Union[DefineType.integer_candidate_input , None]  = None):
        pass


    def elements(self):
        pass

    @property
    def sum(self) -> DefineType.integer_candidate:  # type: ignore
        pass

    @property
    def product(self) -> DefineType.integer_candidate:  # type: ignore
        pass

    def __getitem__(self, index: int) ->  Union[DefineType.Formula , DefineType.Integer] :  # type: ignore
        pass

class NaturalPair(IntegerPair):
    def __init__(self, proof: DefineType.Proof, pair: DefineType.integer_pair_input,  sum:  Union[DefineType.integer_candidate_input , None]  = None, product:  Union[DefineType.integer_candidate_input , None]  = None, gcd:  Union[DefineType.integer_candidate_input , None]  = None, lcm:  Union[DefineType.integer_candidate_input , None]  = None, relational_prime_pairs: list[tuple[DefineType.integer_candidate_input, DefineType.integer_candidate_input]] = []):
        pass


    @property
    def gcd(self) ->  Union[NaturalPair , DefineType.integer_candidate] :  # type: ignore
        pass

    @property
    def gcd_history(self) -> DefineType.Section:  # type: ignore
        pass

    @property
    def lcm(self) ->  Union[DefineType.integer_candidate , None] :  # type: ignore
        pass

    @property
    def product_relation_equation(self) -> DefineType.Equation:  # type: ignore
        pass

    @property
    def summation_relation_equation(self) ->  Union[DefineType.Equation , None] :  # type: ignore
        pass

    def display_gcd_history(self):
        pass

    @overload
    def identify_from_condition(self, sum: int, lcm: None, gcd: int,  section_title: str = '自然数ペアの決定', section_id: str = 'identify_from_condition') -> DefineType.VectorSolutions:  # type: ignore
        ...

    @overload
    def identify_from_condition(self, sum: int, lcm: int, gcd: None = None, section_title: str = '自然数ペアの決定', section_id: str = 'identify_from_condition') -> DefineType.VectorSolutions:  # type: ignore
        ...

    def identify_from_condition(self, sum: int, lcm:  Union[int , None]  = None, gcd:  Union[int , None]  = None, section_title: str = '自然数ペアの決定', section_id: str = 'identify_from_condition') -> DefineType.VectorSolutions:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
