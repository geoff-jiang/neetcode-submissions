class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointers with a set
        # add chars
        # if duplicate, store max length, move left pointer until your each the duplicate letter, removing letters from the set along the way. (don't remove the duplicate)
        # need to check again when you reach the end (maybe no duplicates)

        # cabad

        if len(s) == 0:
            return 0
        
        l = 0
        letter_set = {}
        res = 0

        for r in range(len(s)):
            if s[r] in letter_set: 
                l = max(l, letter_set[s[r]] + 1)
            res = max(res, r - l + 1) 
            letter_set[s[r]] = r
        return res

        
            