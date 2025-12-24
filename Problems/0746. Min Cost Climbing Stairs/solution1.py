# Brute Force
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(index):
            if index >= len(cost):
                return 0
            return cost[index] + min(dfs(index + 1), dfs(index + 2))

        return min(dfs(0), dfs(1))
