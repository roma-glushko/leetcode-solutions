from typing import Dict


class FSObject:
    name: str = ''

    def __init__(self, name: str):
        self.name = name


class Directory(FSObject):
    pass


class File(FSObject):
    pass


class FileSystem:
    """
    Problem Link: https://leetcode.com/problems/design-in-memory-file-system/
    Unlocked Link: http://lixinchengdu.github.io/algorithmbook/leetcode/design-in-memory-file-system.html
    Complexity: Hard
    Locked: true
    """

    filesystem_map: Dict[str, FSObject]

    def __init__(self):
        filesystem_map = {}

    def ls(self, path: str):
        pass

    def mkdir(self, dir_path: str):
        pass

    def addContentToFile(self, file_path: str, content: str):
        pass

    def readContentFromFile(self, file_path: str) -> str:
        pass
