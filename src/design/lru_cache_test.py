from unittest import TestCase

from .lru_cache import LRUCache


class LRUCacheTest(TestCase):

    def test_default_input(self):
        cache = LRUCache(2)

        cache.put(1, 1)  # cache is {1=1}
        cache.put(2, 2)  # cache is {1=1, 2=2}

        self.assertEqual(cache.get(1), 1)

        cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}

        self.assertEqual(cache.get(2), -1)

        cache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}

        self.assertEqual(cache.get(1), -1)

        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)
