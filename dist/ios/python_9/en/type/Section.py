# pyright: reportUnusedImport=false
from __future__ import annotations 
from typing import Union 
from IPython.display import Markdown  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal
from typing import Generator
from typing import overload


class Section:
    """セクション

    引数:
        id(str): id

    """

    def __init__(self, proof: DefineType.Proof, title: str, id: str):
        pass


    def make_sub_section(self, title: str, id: str, index:  Union[int , None]  = None) -> Section:  # type: ignore
        pass

    def __getitem__(self, index: int)-> DefineType.explain:  # type: ignore
        pass

    @overload
    def __setitem__(self, index: int, value: Section) -> Section:  # type: ignore
        ...

    @overload
    def __setitem__(self, index: int, value: DefineType.RelationContent) -> DefineType.RelationContent:  # type: ignore
        ...

    def __setitem__(self, index: int, value:  Union[Section , DefineType.RelationContent] ) ->  Union[Section , DefineType.RelationContent] :  # type: ignore
        pass

    def __iter__(self) -> Generator[DefineType.explain, None, None]:  # type: ignore
        pass

    @overload
    def append(self, content: DefineType.explain, is_therefore_sign: bool = False) -> Section:  # type: ignore
        ...

    @overload
    def append(self, content: DefineType.relation_content, is_therefore_sign: bool = False, appendix: str = '', appendix_type: Literal['because', 'annotate', 'plain'] = 'because') -> Section:  # type: ignore
        ...

    def append(self, content:  Union[DefineType.explain , DefineType.relation_content] , is_therefore_sign: bool = False, appendix: str = '', appendix_type: Literal['because', 'annotate', 'plain'] = 'because') -> Section:  # type: ignore
        pass

    def insert_section(self, section:  Union[Section , str] )->Section:  # type: ignore
        pass

    def display(self, indent_depth: int = 0) -> Section:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
