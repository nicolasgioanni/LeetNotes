# Brute Force
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for start in range(len(gas)):
            total, tank = 0, gas[start]
            current = start
            
            while total < len(gas):
                total += 1
                tank -= cost[current] 
                current = 0 if current + 1 == len(gas) else current + 1
                if tank < 0:
                    break
                tank += gas[current] if total < len(gas) else 0

            if tank >= 0 and total == len(gas):
                return start

        return -1
