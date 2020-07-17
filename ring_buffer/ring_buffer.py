class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []
        self.current = 0

    def append(self, item):
        if len(self.arr) >= self.capacity:
            self.arr[self.current] = item
            if self.current == len(self.arr) - 1:
                self.current = 0
            else:
                self.current += 1
        else:
            self.arr.append(item)

    def get(self):
        return self.arr
