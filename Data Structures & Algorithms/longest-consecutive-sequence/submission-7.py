class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = set(nums)
        res = 0
        for n in c:
            if n-1 not in c:
                streak = 1
                curr = n
                while curr + 1 in c:
                    streak += 1
                    curr += 1
                res = max(res, streak)
        return res
        