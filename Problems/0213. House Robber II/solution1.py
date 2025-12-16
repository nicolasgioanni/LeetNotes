# Brute Force
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(house, houses):
            if house >= len(houses):
                return 0
            elif house > len(houses):
                return 0

            return max(dfs(house + 1, houses), houses[house] + dfs(house + 2, houses))

        option1, option2 = dfs(0, nums[1:]), dfs(0, nums[:-1])

        return max(option1, option2)
