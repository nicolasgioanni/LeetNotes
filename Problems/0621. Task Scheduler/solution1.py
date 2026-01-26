class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26

        for char in tasks:
            counts[ord(char) - ord('A')] += 1

        fmax, cmax = 0, 0

        for count in counts:
            if count > fmax:
                fmax, cmax = count, 1
            elif count == fmax:
                cmax += 1
        
        return max(((fmax - 1) * (n + 1)) + cmax, len(tasks))
