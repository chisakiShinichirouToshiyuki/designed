# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
from IPython.display import Markdown, Math  # type: ignore
from typing import cast
from typing import TYPE_CHECKING
from IPython.display import Markdown  # type: ignore
from typing import Generator
# pyright: reportImportCycles=false


class Equations:
    # def __init__(self, proof: DefineType.Proof, equations:
    #         list[Equation]
    #         | tuple[DefineType.Vector,DefineType.Vector]
    #         # | equation_list_row
    #         # | vector_tuple_row
    #     ):

    def __init__(self, proof: DefineType.Proof, equations:  Union[express_list , express_tuple] ):
        pass


    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    @property
    def equations(self) -> list[DefineType.Equation]:  # type: ignore
        pass

    def add_equation(self, equations: list[DefineType.Equation]):
        pass

    def append(self, equation: DefineType.Equation):
        pass

    def solve(self, focus_terms: set[str] = set()) ->  Union[VectorEquation , None] :  # type: ignore
        pass

    def display(self):
        pass

    def reduce_variable(self, target_variable: str = '', define_equation:  Union[DefineType.Equation , None]  = None) -> Equations:  # type: ignore
        pass

    def __getitem__(self, index: int)-> DefineType.Equation:  # type: ignore
        pass

    def __iter__(self)-> Generator[DefineType.Equation, None, None]:  # type: ignore
        pass

    def __len__(self) -> int:  # type: ignore
        pass

class Solutions(Equations):
    def __init__(self, proof: DefineType.Proof, equations: list[DefineType.Equation] | tuple[DefineType.Vector, DefineType.Vector]):
        pass

    def sort(self, should_reverse: bool = False) -> Solutions:  # type: ignore
        pass

    def display(self):
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def __add__(self, other: Solutions) -> Solutions:  # type: ignore
        """[+] の中置演算子 

        引数:
            other: Vector
        結果: 
            Vector
        """
        pass

class VectorEquation(Equations):
    def __init__(self, proof: DefineType.Proof, equations: list[DefineType.Equation] | tuple[DefineType.Vector, DefineType.Vector]):
        pass


    @property
    def left_side_vector(self) -> DefineType.Vector:  # type: ignore
        pass

    @property
    def right_side_vector(self) -> DefineType.Vector:  # type: ignore
        pass

    def add_equation(self, equations: list[DefineType.Equation]):
        pass

    def append(self, equation: DefineType.Equation):
        pass

    def sort(self, should_reverse: bool = False) -> VectorEquation:  # type: ignore
        pass

    def display(self):
        pass

    def __eq__(self, other: VectorEquation) -> bool:  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
    express_list = list[DefineType.Equation]
    express_tuple = tuple[DefineType.Vector, DefineType.Vector]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
