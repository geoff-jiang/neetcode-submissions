class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        for n in nums:
            if n + 1 in nums:
                temp = 1
                curr = n
                while curr + 1 in nums:
                    temp += 1
                    curr += 1
                if temp > res:
                    res = temp
            if n - 1 in nums:
                temp = 1
                curr = n
                while curr - 1 in nums:
                    curr -= 1
                    temp += 1
                if temp > res:
                    res = temp
        return res

        