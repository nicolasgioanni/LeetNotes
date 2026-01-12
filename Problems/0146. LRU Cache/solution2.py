# Constant Time + Linear Space with Helpers
class LRUCache:

    def __init__(self, capacity: int):
        self.maxC, self.currC = capacity, 0
        self.listMap = {} 
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key in self.listMap:
            self.reorder(key)
            self.update(key)

            return self.listMap[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.listMap: 
            self.reorder(key)
            self.update(key, value)
        else:
            self.append(key, value)
            if len(self.listMap) > self.maxC and self.head is not None: 
                self.remove()

    def reorder(self, key: int) -> None:
        prevN, nextN = self.listMap[key][1:3]
        if prevN is not None: 
            self.listMap[prevN][2] = nextN
        else:
            self.head = nextN
        if nextN is not None: 
            self.listMap[nextN][1] = prevN
        else:
            self.tail = prevN

    def update(self, key: int, value: int = -1) -> None:
        if value != -1: self.listMap[key][0] = value

        if self.tail is not None and self.tail != key:
            self.listMap[key][1:3] = [self.tail, None]
            self.listMap[self.tail][2] = key
            self.tail = key
        else:
            self.head = self.tail = key
            self.listMap[key][1:3] = [None, None]

    def append(self, key: int, value: int) -> None:
        if self.head == None:
            self.head, self.tail = key, key
            self.listMap[key] = [value, None, None] 
        else:
            self.listMap[key] = [value, self.tail, None] 
            self.listMap[self.tail][2] = key
            self.tail = key

    def remove(self) -> None:
        nextHead = self.listMap[self.head][2]
        if nextHead is not None: self.listMap[nextHead][1] = None
        del self.listMap[self.head] 
        self.head = nextHead

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
