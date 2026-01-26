class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.minHeap, self.k = nums, k

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if len(self.minHeap) == self.k:
            heapq.heappushpop(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0]
