class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                oldI, oldN = stack.pop()
                result[oldI] = (i - oldI)
            stack.append([i, n])

        return result
