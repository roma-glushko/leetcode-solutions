class MyCircularQueue:
    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._queue = [0] * capacity

        self._size = 0

        self._head = -1 # the next dequeue position
        self._tail = -1 # the next enqueue position

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. If it's full then return false.
        """
        if self.isFull():
            return False

        self._tail = (self._tail + 1) % self._capacity
        self._queue[self._tail] = value
        self._size += 1

        if self._head == -1:
            self._head = 0

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self._head = (self._head + 1) % self._capacity
        self._size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self._queue[self._head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self._queue[self._tail]

    def isEmpty(self) -> bool:
        return self._size == 0

    def isFull(self) -> bool:
        return self._size >= self._capacity

if __name__ == "__main__":
    # ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]
    # [[3],[1],[2],[3],[4],[],[],[],[4],[]]

    circular_queue = MyCircularQueue(capacity=3)

    # circular_queue.enQueue(1)
    # circular_queue.enQueue(2)
    # circular_queue.enQueue(3)
    # circular_queue.enQueue(4)  # should return False
    # print(circular_queue.Rear())  # should return 3
    # print(circular_queue.isFull())  # should return True
    # circular_queue.deQueue()
    # circular_queue.enQueue(4)
    # print(circular_queue.Rear())  # should return 4

    circular_queue.enQueue(2)
    print(circular_queue.Rear())  # should return 2
    print(circular_queue.Front())  # should return 2
    circular_queue.deQueue()  # should return False
    print(circular_queue.Front())  # should return -1
    circular_queue.deQueue()  # should return False
    print(circular_queue.Front())  # should return -1
    circular_queue.enQueue(4)
    circular_queue.enQueue(2)
    circular_queue.enQueue(2)
    circular_queue.enQueue(3)  # should return False
