# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if buy:
                profit = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                return max(profit, cooldown)
            else:
                sell = prices[i] + dfs(i + 2, True)
                cooldown = dfs(i + 1, False)
                return max(sell, cooldown)

        return dfs(0, True)
