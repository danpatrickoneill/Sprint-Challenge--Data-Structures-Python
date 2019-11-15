class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]


if __name__ == "__main__":

    buffer = RingBuffer(3)

    print(buffer.get())

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    print(buffer.get())

    buffer.append('d')

    print(buffer.get())

    buffer.append('e')
    buffer.append('f')

    print(buffer.get())
