# Linear Time + Constant Space
class Solution:
    def rob(self, nums: List[int]) -> int:
        # [prev2, prev1, n, n+1, n+2...]
        prev2, prev1 = 0, 0

        for n in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + n)
            prev2 = temp

        return prev1
