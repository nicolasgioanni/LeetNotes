class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""

        countS, countT = defaultdict(int), defaultdict(int)
        uniqueChar = 0
        result = ""

        for char in t:
            if countT[char] == 0: uniqueChar += 1
            countT[char] += 1

        l = 0
        for r in range(len(s)):
            countS[s[r]] += 1

            if countS[s[r]] == countT[s[r]]:
                uniqueChar -= 1

            while uniqueChar == 0:
                if not result or r - l + 1 < len(result):
                    result = s[l:r + 1]

                countS[s[l]] -= 1
                if countS[s[l]] < countT[s[l]]:
                    uniqueChar += 1
                
                l += 1

        return result
