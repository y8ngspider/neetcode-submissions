class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def insert(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            lru_node = self.tail.prev
            del self.cache[lru_node.key]
            self.remove(lru_node)
            
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)