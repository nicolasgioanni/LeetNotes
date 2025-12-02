class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], key]
            seen[num] = key
