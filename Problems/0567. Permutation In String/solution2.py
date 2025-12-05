# Dynamic sliding window 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or s1 == "": return True
        if not s2 or s2 == "" or len(s1) > len(s2): return False

        s1Count = [0] * 26
        s1UniqueCharCount = 0
        s1UniqueCharSet = set()

        for char in s1:
            if char not in s1UniqueCharSet:
                s1UniqueCharCount += 1
                s1UniqueCharSet.add(char)
            s1Count[ord(char) - ord("a")] += 1
        
        l, r = 0, 0
        while r < len(s2):
            l = r

            if s2[r] in s1UniqueCharSet:
                s2Count = [0] * 26
                s2UniqueCharCount = 0
                
                while r < len(s2) and s2[r] in s1UniqueCharSet:

                    s2Count[ord(s2[r]) - ord("a")] += 1
                    if s2Count[ord(s2[r]) - ord("a")] == s1Count[ord(s2[r]) - ord("a")]:
                        s2UniqueCharCount += 1
                        
                        if s2UniqueCharCount == s1UniqueCharCount:
                            return True
                    while s2Count[ord(s2[r]) - ord("a")] > s1Count[ord(s2[r]) - ord("a")]:
                        if s2Count[ord(s2[l]) - ord("a")] == s1Count[ord(s2[l]) - ord("a")]:
                            s2UniqueCharCount -= 1
                        s2Count[ord(s2[l]) - ord("a")] -= 1
                        l += 1

                    r += 1

            r += 1



        return False
