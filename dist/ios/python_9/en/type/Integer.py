# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations 
from typing import Union 
# from typing import TYPE_CHECKING
from typing import Literal
import math
from typing import overload


class Integer:
    def __init__(self, proof: DefineType.Proof, express: int):
        pass


    @property
    def variables(self) -> set[str]:  # type: ignore
        pass

    @property
    def degree(self) -> int:  # type: ignore
        """式の最大の次数

        注意:
            整数多項式以外は、正しい結果を返さない。
            例）(x**2 + (1/x)**5) -> 5
        """
        pass

    @property
    def text(self) -> str:  # type: ignore
        pass

    @property
    def ast(self) -> Ast.Ast:  # type: ignore
        pass

    @property
    def is_integer(self) ->  Union[bool , None] :  # type: ignore
        pass

    @property
    def number(self) -> int:  # type: ignore
        pass

    @property
    def is_prime(self) -> bool:  # type: ignore
        pass

    @property
    def divisor_quantity(self) -> Integer:  # type: ignore
        pass

    @property
    def divisor_summary(self) -> Integer:  # type: ignore
        pass

    @property
    def divisors(self) -> list[int]:  # type: ignore
        pass

    @staticmethod
    def proof_root_is_rational_2_root_is_integer(proof: DefineType.Proof, root: str = 'm', numerator: str = 'q', denominator: str = 'l', section_title: str = "無理数の証明") -> bool:  # type: ignore
        pass

    @staticmethod
    def proof_prime_exist_indefinitely(proof: DefineType.Proof, section_title: str = '素数が無限にある証明', section_id: str = 'proof_prime_exist_indefinitely'):
        pass

    def prime_factorize(self) -> dict[int, int]:  # type: ignore
        pass

    def get_primes_up_to_self(self) -> list[int]:  # type: ignore
        pass

    def can_cast(self, type: type[DefineType.Float] | type[DefineType.Fraction]) -> bool:  # type: ignore
        pass

    def get_coefficients(self, focus_variable: str, should_limit_integer: bool = False) -> list[Integer]:  # type: ignore
        pass

    @overload
    def is_relatively_prime(self, other:  Union[Integer , int] , relational_prime_pairs: list[tuple[ Union[int , Integer , DefineType.Formula] ,  Union[int , Integer , DefineType.Formula] ]] = []) -> bool:  # type: ignore
        ...

    @overload
    def is_relatively_prime(self, other: DefineType.Formula, relational_prime_pairs: list[tuple[ Union[int , Integer , DefineType.Formula] ,  Union[int , Integer , DefineType.Formula] ]] = []) ->  Union[bool , None] :  # type: ignore
        ...

    def is_relatively_prime(self, other:  Union[Integer , int]  | DefineType.Formula, relational_prime_pairs: list[tuple[ Union[int , Integer , DefineType.Formula] ,  Union[int , Integer , DefineType.Formula] ]] = []) ->  Union[bool , None] :  # type: ignore
        pass

    def get_split_pair_in_to_product(self, uniqueness: Literal['combination', 'order'] = 'order', is_include_minus: bool = False) -> set[tuple[int, int]]:  # type: ignore
        pass

    def __eq__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Equation] :  # type: ignore
        pass

    def __ne__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Unequation] :  # type: ignore
        pass

    def __lt__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __le__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __gt__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __ge__(self, other: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Inequation] :  # type: ignore
        pass

    def __format__(self, __format_spec: str) -> str:  # type: ignore
        pass

    def display(self):
        pass

    def __str__(self) -> str:  # type: ignore
        pass

    @overload
    def __rshift__(self, type: type[DefineType.Float]) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Formula]) -> DefineType.Formula:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[DefineType.Fraction]) -> DefineType.Fraction:  # type: ignore
        ...

    @overload
    def __rshift__(self, type: type[Integer]) -> Integer:  # type: ignore
        ...

    def __rshift__(self, type: type[DefineType.Float] | type[DefineType.Formula] | type[DefineType.Fraction] | type[Integer]) ->  Union[DefineType.Formula , DefineType.Float , DefineType.Fraction , Integer] :  # type: ignore
        pass

    @overload
    def __add__(self, other:  Union[Integer , int] ) -> Integer:  # type: ignore
        ...

    @overload
    def __add__(self, other: DefineType.Fraction) -> DefineType.Fraction:  # type: ignore
        ...

    @overload
    def __add__(self, other:  Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __add__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __add__(self, other:  Union[Integer , int]  |  Union[DefineType.Float , float]  | DefineType.Fraction | DefineType.Formula) ->  Union[Integer , DefineType.Float , DefineType.Formula , DefineType.Fraction] :  # type: ignore
        pass

    @overload
    def __sub__(self, other:  Union[Integer , int] ) -> Integer:  # type: ignore
        ...

    @overload
    def __sub__(self, other: DefineType.Fraction) -> DefineType.Fraction:  # type: ignore
        ...

    @overload
    def __sub__(self, other:  Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __sub__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __sub__(self, other:  Union[Integer , int]  |  Union[DefineType.Float , float]  | DefineType.Fraction | DefineType.Formula) ->  Union[Integer , DefineType.Float , DefineType.Formula , DefineType.Fraction] :  # type: ignore
        pass

    def __neg__(self) -> Integer:  # type: ignore
        pass

    @overload
    def __mul__(self, other:  Union[Integer , int] ) -> Integer:  # type: ignore
        ...

    @overload
    def __mul__(self, other: DefineType.Fraction) -> DefineType.Fraction:  # type: ignore
        ...

    @overload
    def __mul__(self, other:  Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __mul__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mul__(self, other:  Union[Integer , int]  |  Union[DefineType.Float , float]  | DefineType.Fraction | DefineType.Formula) ->  Union[Integer , DefineType.Float , DefineType.Formula , DefineType.Fraction] :  # type: ignore
        pass

    @overload
    def __truediv__(self, other:  Union[Integer , int]  | DefineType.Fraction) ->  Union[DefineType.Fraction , Integer] :  # type: ignore
        ...

    @overload
    def __truediv__(self, other:  Union[DefineType.Float , float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __truediv__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __truediv__(self, other:  Union[Integer , int]  |  Union[DefineType.Float , float]  | DefineType.Fraction | DefineType.Formula) -> DefineType.Float | DefineType.Formula |  Union[DefineType.Fraction , Integer] :  # type: ignore
        pass

    @overload
    def __mod__(self, other:  Union[Integer , int] ) -> Integer:  # type: ignore
        ...

    @overload
    def __mod__(self, other: DefineType.Fraction) ->  Union[Integer , DefineType.Fraction] :  # type: ignore
        ...

    @overload
    def __mod__(self, other:  Union[float , DefineType.Float] ) -> DefineType.Float:  # type: ignore
        ...

    @overload
    def __mod__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __mod__(self, other:  Union[DefineType.Formula , float , int , Integer , DefineType.Float , DefineType.Fraction] ) ->  Union[Integer , DefineType.Float , DefineType.Fraction , DefineType.Formula] :  # type: ignore
        """[%] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __floordiv__(self, other:  Union[Integer , int]  |  Union[DefineType.Float , float]  | DefineType.Fraction) -> Integer:  # type: ignore
        ...

    @overload
    def __floordiv__(self, other: DefineType.Formula) -> DefineType.Formula:  # type: ignore
        ...

    def __floordiv__(self, other:   Union[DefineType.Formula , float , int , Integer , DefineType.Float , DefineType.Fraction] ) ->  Union[DefineType.Formula , Integer] :  # type: ignore
        """[//] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __pow__(self, other:  Union[Integer , int] ) -> Integer:  # type: ignore
        ...

    @overload
    def __pow__(self, other: DefineType.Formula |  Union[float , DefineType.Float]  | DefineType.Fraction) -> DefineType.Formula:  # type: ignore
        ...

    def __pow__(self, other:   Union[DefineType.Formula , float , int , Integer , DefineType.Float , DefineType.Fraction] ) ->  Union[Integer , DefineType.Formula] :  # type: ignore
        """[**] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __radd__(self, other:  Union[int , Integer] ) -> Integer:  # type: ignore
        ...

    @overload
    def __radd__(self, other:  float) -> DefineType.Float:  # type: ignore
        ...

    def __radd__(self, other: float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Float] :  # type: ignore
        """[+] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rsub__(self, other:  Union[int , Integer] ) -> Integer:  # type: ignore
        ...

    @overload
    def __rsub__(self, other:  float) -> DefineType.Float:  # type: ignore
        ...

    def __rsub__(self, other: float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Float] :  # type: ignore
        """[-] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rmul__(self, other:  Union[int , Integer] ) -> Integer:  # type: ignore
        ...

    @overload
    def __rmul__(self, other:  float) -> DefineType.Float:  # type: ignore
        ...

    def __rmul__(self, other: float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Float] :  # type: ignore
        """[*] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rtruediv__(self, other:  Union[int , Integer] ) ->  Union[Integer , DefineType.Fraction] :  # type: ignore
        ...

    @overload
    def __rtruediv__(self, other:  float) -> DefineType.Float:  # type: ignore
        ...

    def __rtruediv__(self, other: float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Fraction]  | DefineType.Float:  # type: ignore
        """[/] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rpow__(self, other:  Union[int , Integer] ) -> Integer:  # type: ignore
        ...

    @overload
    def __rpow__(self, other:  float) -> DefineType.Formula:  # type: ignore
        ...

    def __rpow__(self, other: float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Formula] :  # type: ignore
        """[**] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    @overload
    def __rmod__(self, other:  Union[int , Integer] ) -> Integer:  # type: ignore
        ...

    @overload
    def __rmod__(self, other:  float) -> DefineType.Float:  # type: ignore
        ...

    def __rmod__(self, other:  float |  Union[int , Integer] ) ->  Union[Integer , DefineType.Float] :  # type: ignore
        """[%] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __rfloordiv__(self, other:   Union[float , int] ) -> Integer:  # type: ignore
        """[//] の中置演算子 

        引数:
            other: 式
        結果: 
            Formula
        """
        pass

    def __eq__(self, term: DefineType.term_) ->  Union[DefineType.SymbolicBool , DefineType.Equation] :  # type: ignore
        pass

    def get_powered_residual(self, power: int, mod: int, _range: tuple[int, int] = (1, 5)):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
