class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for char in range(len(s)):
            count[ord(s[char]) - ord('a')] += 1
            count[ord(t[char]) - ord('a')] -= 1

        for charCount in range(len(count)):
            if count[charCount] != 0:
                return False

        else: 
            return True
