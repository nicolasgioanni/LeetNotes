class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "!" + s

        return result

    def decode(self, s: str) -> List[str]:
        if s == None or s == "":
            return []

        result = []
        l, r = 0, 0

        while r < len(s):
            while s[r] != "!" and r < len(s):
                r += 1
            length = int(s[l:r])

            l = r + 1
            r = l + length

            result.append(s[l:r])
            l = r
            
        return result
