# DP Optimal Time + Space
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[amount] = 1

        for coin in coins:
            for i in range(amount - 1, -1, -1):
                dp[i] += dp[i + coin] if coin + i <= amount else 0
        
        return dp[0]
