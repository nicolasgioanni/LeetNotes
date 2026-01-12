# Constant Time + Linear Space without Helpers
class LRUCache:

    def __init__(self, capacity: int):
        self.maxC, self.currC = capacity, 0
        self.listMap = {} 
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key in self.listMap:
            self.reorder(key)
            return self.listMap[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.listMap: 
            self.reorder(key, value)
        else:
            if not self.head:
                self.head, self.tail = key, key
                self.listMap[key] = [value, None, None] 
            else:
                self.listMap[key] = [value, self.tail, None] 
                if self.tail: self.listMap[self.tail][2] = key
                self.tail = key

            if self.currC + 1 > self.maxC and self.head:
                nextHead = self.listMap[self.head][2]
                if nextHead: self.listMap[nextHead][1] = None
                del self.listMap[self.head] 
                self.head = nextHead
            else:
                self.currC += 1

    def reorder(self, key: int, value: int = -1) -> None:
        prevN, nextN = self.listMap[key][1:3]
        if prevN: 
            self.listMap[prevN][2] = nextN
        else:
            self.head = nextN
        if nextN: 
            self.listMap[nextN][1] = prevN
        else:
            self.tail = prevN

        if value != -1: self.listMap[key][0] = value

        if self.tail:
            self.listMap[key][1:3] = [self.tail, None]
            self.listMap[self.tail][2] = key
            self.tail = key
        else:
            self.head = self.tail = key
