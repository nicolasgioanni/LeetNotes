class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for num, count in counts.items():
            frequency[count].append(num)

        result = []

        for i in range(len(frequency) - 1, -1, -1):
            for num in frequency[i]:
                result.append(num)

                if len(result) == k:
                    return result
