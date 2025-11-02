import dataclasses


@dataclasses.dataclass # TODO: could have been a simple tuple (key, value)
class MapItem:
    key: int
    value: int

class MyHashMap:
    def __init__(self, init_buckets: int = 2048, load_factor: float = 0.75) -> None:
        self._size = 0
        self._load_factor = load_factor

        self._capacity = init_buckets
        self._buckets = [] # TODO: learn about open addressing
        self._resize_threshold = 0

        self._resize(init_buckets)

    def put(self, key: int, value: int) -> None:
        bucket = self._bucket_by_key(key)

        for item in bucket:
            if item.key == key:
                item.value = value
                return

        if self._size + 1 > self._resize_threshold:
            self._resize(self._capacity * 2)
            bucket = self._bucket_by_key(key) # bucket may change after resizing

        self._size += 1
        bucket.append(MapItem(key, value))

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets

        self._capacity = new_capacity
        self._buckets = [[] for _ in range(self._capacity)]
        self._resize_threshold = int(self._capacity * self._load_factor)

        for bucket in old_buckets:
            for item in bucket:
                new_bucket = self._bucket_by_key(item.key)
                new_bucket.append(item)

    def get(self, key: int) -> int:
        bucket = self._bucket_by_key(key)

        for item in bucket:
            if item.key == key:
                return item.value

        return -1

    def remove(self, key: int) -> None:
        bucket = self._bucket_by_key(key)

        for i, item in enumerate(bucket):
            if item.key == key:
                del bucket[i]
                self._size -= 1
                return

    def _bucket_by_key(self, key: int) -> list[MapItem]:
        idx = self._index(key)
        return self._buckets[idx]

    def _index(self, key: int) -> int:
        return hash(key) % self._capacity # (hash(key) + capacity) % capacity

if __name__ == '__main__':
    hashmap = MyHashMap()

    hashmap.put(1, 1)
    hashmap.put(2, 2)

    print(hashmap.get(2))