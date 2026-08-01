class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.value = value
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
            return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
        elif key not in self.cache and self.capacity == 0:
            self.cache[key] = Node(key,value)
            lru_node = self.tail.prev
            lru_node.prev.next = self.tail
            self.tail.prev = lru_node.prev
            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
            del self.cache[lru_node.key]
        else:
            self.cache[key] = Node(key,value)
            self.cache[key].next = self.head.next
            self.cache[key].prev = self.head
            self.head.next.prev = self.cache[key]
            self.head.next = self.cache[key]
            self.capacity -= 1