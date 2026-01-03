# Pruned Brute Force
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def dfs(moneyLeft, index):
            if moneyLeft == 0:
                return 1
            elif index == len(coins):
                return 0
            elif (moneyLeft, index) in dp:
                return dp[(moneyLeft, index)]
            
            ways = 0
            for i in range(index, len(coins)):
                if moneyLeft - coins[i] >= 0:
                    ways += dfs(moneyLeft - coins[i], i)
            
            dp[(moneyLeft, index)] = ways
            return ways

        return dfs(amount, 0)
