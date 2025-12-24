# DP Optimal Solution O(n * m), O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(1 + dp[i - coin], dp[i])

        return dp[amount] if dp[amount] != amount + 1 else -1
