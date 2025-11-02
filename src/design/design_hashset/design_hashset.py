Bucket = list[int]

class MyHashSet:
    def __init__(self, init_buckets: int = 2048, load_factor: float = 0.75) -> None:
        self._bucket_count = init_buckets
        self._load_factor = load_factor

        self._buckets: list[Bucket] = []
        self._resize_threshold = 0
        self._size = 0

        self._resize(init_buckets)

    def add(self, key: int) -> None:
        bucket = self._bucket_by_key(key)

        if key in bucket:
            return

        if self._size + 1 > self._resize_threshold:
            self._resize(self._bucket_count * 2)
            bucket = self._bucket_by_key(key)

        self._size += 1
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._bucket_by_key(key)

        for idx, item in enumerate(bucket):
            if item == key:
                del bucket[idx]
                self._size -= 1
                return

    def contains(self, key: int) -> bool:
        bucket = self._bucket_by_key(key)

        return key in bucket

    def __len__(self) -> int:
        return self._size

    def _bucket_by_key(self, key: int) -> Bucket:
        idx = hash(key) % self._bucket_count
        return self._buckets[idx]

    def _resize(self, new_bucket_count: int) -> None:
        old_buckets = self._buckets

        self._resize_threshold = int(new_bucket_count * self._load_factor)
        self._bucket_count = new_bucket_count
        self._buckets = [[] for _ in range(new_bucket_count)]

        for bucket in old_buckets:
            for key in bucket:
                new_bucket = self._bucket_by_key(key)
                new_bucket.append(key)


if __name__ == '__main__':
    hset = MyHashSet()

    hset.add(1)

    print(hset.contains(2))
    print(hset.contains(1))