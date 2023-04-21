# pyright: reportUnusedImport=false
class DefineType(object):
    def __getattribute__(self, name: str):
        return str
