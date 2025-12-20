# Optimal Space + Time 
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for char in range(len(s)):
            l, r = char, char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l, r = l - 1, r + 1

            l, r = char, char + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l, r = l - 1, r + 1

        return result
