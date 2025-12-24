# Brute Force
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(money):
            if money == amount:
                return 0
            else:
            
                result = amount + 1
                for coin in coins:
                    if coin + money <= amount:
                        result = min(1 + dfs(coin + money), result)
                
                return result

        answer = dfs(0)
        return -1 if answer == amount + 1 else answer
