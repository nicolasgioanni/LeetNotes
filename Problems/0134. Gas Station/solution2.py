# Linear Time + Constant Space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, index = 0, -1

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            
            if total >= 0:
                index = i if index == -1 else index
            else:
                total, index = 0, -1

        return index
