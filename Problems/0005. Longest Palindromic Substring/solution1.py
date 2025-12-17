# Brute Force O(n^3)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        
        def isPalindrome(st):
            l, r = 0, len(st) - 1

            while l < r:
                if st[l] != st[r]:
                    return False
                else:
                    l, r = l + 1, r - 1   
            
            return True


        for l in range(len(s)):
            for r in range(l + 2, len(s) + 1):
                if isPalindrome(s[l:r]) and r - l > len(result):
                    result = s[l:r]


        return s[0] if not result else result
