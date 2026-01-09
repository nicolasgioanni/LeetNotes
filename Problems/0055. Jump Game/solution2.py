# Linear Time + Constant Space
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            goal = i if nums[i] + i >= goal else goal
        
        return True if goal == 0 else False
