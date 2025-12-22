# Optimal Space + Time
class Solution:
    def numDecodings(self, s: str) -> int:
        current, ways1, ways2 = 0, 1, 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                current = 0
            else:
                current = ways1

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] < "7")):
                current += ways2

            current, ways1, ways2 = 0, current, ways1

        
        return ways1
