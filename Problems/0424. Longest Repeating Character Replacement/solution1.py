class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        mostFrequent = 0
        longest = 0

        l = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord("A")] += 1
            
            if count[ord(s[r]) - ord("A")] > mostFrequent:
                mostFrequent = count[ord(s[r]) - ord("A")]

            while mostFrequent + k < r - l + 1:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            
        return longest
