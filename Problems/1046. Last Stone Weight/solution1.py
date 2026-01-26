class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            first = -maxHeap[0]
            heapq.heappop(maxHeap)

            second = -maxHeap[0]
            heapq.heappop(maxHeap)

            smashed = first - second
            if smashed != 0:
                heapq.heappush(maxHeap, -smashed)
            
        return -maxHeap[0] if len(maxHeap) > 0 else 0
