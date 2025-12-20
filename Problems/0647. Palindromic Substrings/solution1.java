# Brute Force O(n^3)
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def isPalindrome(s2: str) -> bool:
            l, r = 0, len(s2) - 1

            while l < r:
                while l < r and not s2[l].isalnum():
                    l += 1
                while l < r and not s2[r].isalnum():
                    r -= 1

                if s2[l] != s2[r]:
                    return False
                
                l, r = l + 1, r - 1

            return True

        for l in range(len(s)):
            for r in range(l, len(s)):
                if isPalindrome(s[l:r + 1]):
                    result += 1

        return result
