class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        pair = [(p, s) for p, s in zip(position, speed)]

        for p, s in sorted(pair, reverse=True):
            if stack and stack[-1] >= ((target - p) / s):
                continue
            else:
                stack.append((target - p) / s)
        return len(stack)
