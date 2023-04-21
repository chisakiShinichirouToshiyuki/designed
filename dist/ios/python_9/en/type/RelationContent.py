# pyright: reportUnusedImport=false
from __future__ import annotations 
from typing import Union 
from IPython.display import Markdown, Math  # type: ignore
from typing import TYPE_CHECKING
from typing import Literal


class RelationContent:
    def __init__(self, content: DefineType.relation_content, is_therefore_sign: bool = False, appendix: str = '', appendix_type: Literal['because', 'annotate', 'plain'] = 'because'):
        pass


    @property
    def content(self) -> DefineType.relation_content:  # type: ignore
        pass

    @property
    def ascended_therefore_sign(self) -> bool:  # type: ignore
        pass


    @property
    def display(self, indent_depth: int = 0, previous_content:  Union[RelationContent , None]  = None, omit_mode: Literal['off', 'on', 'auto'] = 'auto'):
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    from . import DefineType
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
