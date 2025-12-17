# Linear Time + Constant Space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def tryRob(house, numbers):
            prev2, prev1 = 0, 0

            for i in range(len(numbers)):
                temp = prev1
                prev1 = max(prev2 + numbers[i], prev1)
                prev2 = temp

            return prev1


        return max(tryRob(0, nums[1:]), tryRob(0, nums[:-1]))
