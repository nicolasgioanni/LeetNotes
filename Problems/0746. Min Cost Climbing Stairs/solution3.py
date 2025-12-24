# DP Bottom-up/Linear Time + Constant Space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            prev1, prev2 = cost[i] + min(prev1, prev2), prev1

        return min(prev1, prev2)
