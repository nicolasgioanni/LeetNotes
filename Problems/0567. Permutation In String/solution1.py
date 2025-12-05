# Fixed sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        count1, count2 = [0] * 26, [0] * 26
        matches = 0

        for r in range(len(s1)):
            count1[ord(s1[r]) - ord('a')] += 1
            count2[ord(s2[r]) - ord('a')] += 1

        for r in range(26):
            matches += 1 if count1[r] == count2[r] else 0

        l = 0
        for r in range(len(s1), len(s2), 1):
            if matches == 26: return True

            count2[ord(s2[r]) - ord('a')] += 1
            if count2[ord(s2[r]) - ord('a')] == count1[ord(s2[r]) - ord('a')]:
                matches += 1
            elif count2[ord(s2[r]) - ord('a')] - 1 == count1[ord(s2[r]) - ord('a')]:
                matches -= 1

            count2[ord(s2[l]) - ord('a')] -= 1
            if count2[ord(s2[l]) - ord('a')] == count1[ord(s2[l]) - ord('a')]:
                matches += 1
            elif count2[ord(s2[l]) - ord('a')] + 1 == count1[ord(s2[l]) - ord('a')]:
                matches -= 1

            l += 1
        return matches == 26
