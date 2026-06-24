class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dq = deque()


    def get(self, key: int) -> int:
        if key in self.cache:
            self.dq.remove(key)
            self.dq.appendleft(key)
            return self.cache[key]
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dq.remove(key)
        elif len(self.cache) >= self.capacity:
            rem = self.dq.pop()
            self.cache.pop(rem)
        self.dq.appendleft(key)
        self.cache[key] = value
