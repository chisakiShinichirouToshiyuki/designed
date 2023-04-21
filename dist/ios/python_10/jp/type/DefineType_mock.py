# pyright: reportUnusedImport=false
class 型定義クラス(object):
    def __getattribute__(self, name: str):
        return str
