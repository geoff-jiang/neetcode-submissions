class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # dp with a dict? 
        # for each number, check if num - 1 exists in nums and if yes, add 1 to the previous result. 
        # return max of the dict? 
        

        nums_set = set(nums)

        res = 0

        for n in nums: 
            if n - 1 not in nums_set:
                j = n
                curr  = 1
                while j + 1 in nums_set:
                    curr += 1
                    j += 1
                res = max(res, curr)
        return res