class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numHeap = nums
        self.k = k

        heapq.heapify(self.numHeap)
        while len(self.numHeap) > self.k:
            heapq.heappop(self.numHeap)

    def add(self, val: int) -> int:
        if len(self.numHeap) == self.k:
            heapq.heappushpop(self.numHeap, val)
        else:
            heapq.heappush(self.numHeap, val)

        return self.numHeap[0]
