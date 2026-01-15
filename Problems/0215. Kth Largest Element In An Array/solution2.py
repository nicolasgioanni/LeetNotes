class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            else:
                heapq.heappushpop(minHeap, n)

        return minHeap[0]
