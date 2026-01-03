# Brute Force
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def dfs(moneyLeft, avaliableCoins):
            if moneyLeft == 0:
                return 1
            
            ways = 0
            for i in range(len(avaliableCoins)):
                if moneyLeft - avaliableCoins[i] >= 0:
                    ways += dfs(moneyLeft - avaliableCoins[i], avaliableCoins[i:])
            
            return ways

        return dfs(amount, coins)
