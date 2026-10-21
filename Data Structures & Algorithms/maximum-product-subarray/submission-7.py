class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]
        # curMin, curMax = 1, 1

        # for n in nums:
        #     tmp = curMax * n
        #     curMax = max(curMax * n, curMin * n, n) 
        #     curMin = min(curMin * n, n, tmp)
        #     res = max(res, curMax)
        # return res

        prefix, suffix = 0, 0

        res = nums[0]

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) -1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res