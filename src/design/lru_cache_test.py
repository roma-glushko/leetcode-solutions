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

    def test_put_items_only(self):
        cache = LRUCache(3)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)

        cache.put(4, 4)
        cache.put(5, 5)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), -1)

        cache.put(6, 6)
        self.assertEqual(cache.get(3), -1)

        self.assertEqual(cache.get(4), 4)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(6), 6)

    def test_single_item_capacity(self):
        cache = LRUCache(1)

        cache.put(2, 1)

        self.assertEqual(cache.get(1), -1)

    def test_item_replacing(self):
        cache = LRUCache(2)

        cache.put(2, 1)
        cache.put(2, 2)

        self.assertEqual(cache.get(2), 2)

    def test_zero_values(self):
        cache = LRUCache(2)

        cache.put(1, 0)
        cache.put(2, 2)

        self.assertEqual(cache.get(1), 0)

        cache.put(3, 3)

        self.assertEqual(cache.get(2), -1)

        cache.put(4, 4)

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_long_list_of_values(self):
        cache = LRUCache(10)

        for (key, value) in [[10, 13], [3, 17], [6, 11], [10, 5], [9, 10]]:
            cache.put(key, value)

        self.assertEqual(cache.get(13), -1)

        cache.put(2, 19)

        self.assertEqual(cache.get(2), 19)
        self.assertEqual(cache.get(3), 17)

        cache.put(5, 25)

        self.assertEqual(cache.get(8), -1)

        for (key, value) in [[9, 22], [5, 5], [1, 30]]:
            cache.put(key, value)

        self.assertEqual(cache.get(11), -1)

        cache.put(9, 12)

        self.assertEqual(cache.get(7), -1)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(8), -1)
        self.assertEqual(cache.get(9), 12)

        cache.put(4, 30)
        cache.put(9, 3)

        self.assertEqual(cache.get(9), 3)
        self.assertEqual(cache.get(10), 5)
        self.assertEqual(cache.get(10), 5)

        cache.put(6, 14)
        cache.put(3, 1)

        self.assertEqual(cache.get(3), 1)

        cache.put(10, 11)

        self.assertEqual(cache.get(8), -1)

        cache.put(2, 14)

        self.assertEqual(cache.get(1), 30)
        self.assertEqual(cache.get(5), 5)
        self.assertEqual(cache.get(4), 30)

        for (key, value) in [[11, 4], [12, 24], [5, 18]]:
            cache.put(key, value)

        self.assertEqual(cache.get(13), -1)

        cache.put(7, 23)

        self.assertEqual(cache.get(8), -1)
        self.assertEqual(cache.get(12), 24)

        cache.put(3, 27)
        cache.put(2, 12)

        self.assertEqual(cache.get(5), 18)

        for (key, value) in [[2, 9], [13, 4], [8, 18], [1, 7]]:
            cache.put(key, value)

        self.assertEqual(cache.get(6), -1)

        cache.put(9, 29)
        cache.put(8, 21)

        self.assertEqual(cache.get(5), 18)

        cache.put(6, 30)
        cache.put(1, 12)

        self.assertEqual(cache.get(10), -1)

        for (key, value) in [[4, 15], [7, 22], [11, 26], [8, 17], [9, 29]]:
            cache.put(key, value)

        self.assertEqual(cache.get(5), 18)

        cache.put(3, 4)
        cache.put(11, 30)

        self.assertEqual(cache.get(12), -1)

        cache.put(4, 29)

        self.assertEqual(cache.get(3), 4)
        self.assertEqual(cache.get(9), 29)
        self.assertEqual(cache.get(6), 30)

        cache.put(3, 4)

        self.assertEqual(cache.get(1), 12)
        self.assertEqual(cache.get(10), -1)

        cache.put(3, 29)
        cache.put(10, 28)
        cache.put(1, 20)
        cache.put(11, 13)

        self.assertEqual(cache.get(3), 29)

        cache.put(3, 12)
        cache.put(3, 8)
        cache.put(10, 9)
        cache.put(3, 26)

        self.assertEqual(cache.get(8), 17)
        self.assertEqual(cache.get(7), 22)
        self.assertEqual(cache.get(5), 18)

        cache.put(13, 17)
        cache.put(2, 27)
        cache.put(11, 15)

        self.assertEqual(cache.get(12), -1)

        for (key, value) in [[9, 19], [2, 15], [3, 16]]:
            cache.put(key, value)

        self.assertEqual(cache.get(1), 20)

        for (key, value) in [[12, 17], [9, 1], [6, 19]]:
            cache.put(key, value)

        self.assertEqual(cache.get(4), -1)
        self.assertEqual(cache.get(5), 18)
        self.assertEqual(cache.get(5), 18)

        for (key, value) in [[8, 1], [11, 7], [5, 2], [9, 28]]:
            cache.put(key, value)

        self.assertEqual(cache.get(1), 20)

        for (key, value) in [[2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]:
            cache.put(key, value)
