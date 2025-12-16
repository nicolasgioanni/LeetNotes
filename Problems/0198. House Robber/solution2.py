# Linear Time + Space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        cache = [0] * len(nums)
        cache[0] = nums[0]
        cache[1] = max(nums[0], nums[1])

        for i in range(2, len(nums), 1):
            cache[i] = max(cache[i - 2] + nums[i], cache[i - 1])

        return cache[-1]
