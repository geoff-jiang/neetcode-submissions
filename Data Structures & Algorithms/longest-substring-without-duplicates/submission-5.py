class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        indexMap = {s[0]: 0}
        l, r = 0, 1

        res = 0

        while r < len(s):
            if s[r] in indexMap:
                res = max(res, r - l)
                l = max(l, indexMap[s[r]] + 1)
            indexMap[s[r]] = r
            r += 1
        return max(res, r - l)

        