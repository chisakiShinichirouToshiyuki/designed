# pyright: reportUnusedImport=false
# pyright: reportImportCycles=false
from __future__ import annotations
from IPython.display import Markdown, Math  # type: ignore
from typing import Literal
from typing import overload
from typing import TYPE_CHECKING
import random


class Proof:
    """証明における説明、変数を管理するクラス
    """


    def __init__(self):
        """コンストラクタ
        """
        pass

    @property
    def variables(self) -> DefineType.variables:  # type: ignore
        pass

    @property
    def section_titles(self) -> list[str]:  # type: ignore
        """_summary_

        Returns:
            list[str]: _description_
        """
        pass

    def get_section(self, title: str) -> DefineType.Section:  # type: ignore
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

    def make_temporary_variable(self) -> DefineType.Formula:  # type: ignore
        pass

    def make_temporary_section_id(self, base_id: str) -> str:  # type: ignore
        pass

    @overload
    def get_variable(self, variable: list[str] | set[str]) -> list[DefineType.Formula]:  # type: ignore
        ...

    @overload
    def get_variable(self, variable: str) -> DefineType.Formula:  # type: ignore
        ...

    def get_variable(self, variable: str | variables_list | variables_set) -> DefineType.Formula | formulas:  # type: ignore
        pass

    def update_variables(self, variables: DefineType.variables):
        pass

    @overload
    def make_variable(self, variables: str, variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}) -> DefineType.Formula:  # type: ignore
        ...

    @overload
    def make_variable(self, variables: variables_list, variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}) -> formulas:  # type: ignore
        ...

    def make_variable(self, variables: str | variables_list, variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}) -> DefineType.Formula | formulas:  # type: ignore
        pass

    def make_variables(self, variables: str, variable_types: DefineType.variable_type_optional | DefineType.variable_types_optional = {}) -> formulas:  # type: ignore
        pass

    def register_variables(self, variables: list[str], variable_types: DefineType.variable_types_optional = {}):
        pass

    def make_section(self, title: str, id: str) -> DefineType.Section:  # type: ignore
        pass

    @overload
    def append_explain(self, content: DefineType.explain, section: str = '') -> Proof:  # type: ignore
        ...

    @overload
    def append_explain(self, content: DefineType.relation_content, section: str = '', is_therefore_sign: bool = False, appendix: str = '', appendix_type: Literal['because', 'annotate', 'plain'] = 'because') -> Proof:  # type: ignore
        ...

    def append_explain(self,  content: DefineType.explain | DefineType.relation_content, section: str = '', is_therefore_sign: bool = False, appendix: str = '', appendix_type: Literal['because', 'annotate', 'plain'] = 'because') -> Proof:  # type: ignore
        pass

    def insert_section(self, section: DefineType.Section | str, parent_section: str | DefineType.Section | None = None) -> Proof:  # type: ignore
        pass

    def display_explain(self, section: str = '') -> Proof:  # type: ignore
        pass

# 型チェック時のみimportし、実行時の循環Importエラーを回避
if TYPE_CHECKING:
    import DefineType
    variables_list = list[str]
    variables_set = set[str]
    formulas = list[DefineType.Formula]
else:
    from . import DefineType_mock
    DefineType = DefineType_mock.DefineType()
