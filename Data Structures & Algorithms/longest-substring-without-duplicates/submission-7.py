class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # aabc
        # abca
        # abacd
        # bacade

        char_set = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] in char_set:
                res = max(res, r - l)
                while s[l] != s[r]:
                    char_set.remove(s[l])
                    l += 1
                l += 1
            res = max(res, r - l + 1)
            char_set.add(s[r])
            r += 1
        
        return res



        