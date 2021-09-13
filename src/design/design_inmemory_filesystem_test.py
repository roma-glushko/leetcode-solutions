from unittest import TestCase

from .design_inmemory_filesystem import FileSystem


class DesignInMemoryFilesystemTest(TestCase):
    def test_default_input(self):
        fs: FileSystem = FileSystem()

        self.assertEqual(fs.ls("/"), [])

        fs.mkdir("/a/b/c")
        fs.addContentToFile("/a/b/c/d", "hello")

        self.assertEqual(fs.ls("/"), ["a"])
        self.assertEqual(fs.readContentFromFile("/a/b/c/d"), "hello")
