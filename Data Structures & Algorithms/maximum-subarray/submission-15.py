class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)

        # memo = [[0] * 2 for _ in range(n)]

        # memo[n-1][1], memo[n-1][0] = nums[n-1], nums[n-1]

        # for i in range(n-2, -1, -1):
        #     memo[i][1] = max(nums[i] + memo[i + 1][1], nums[i])
        #     memo[i][0] = max(memo[i][1], memo[i + 1][0])
        
        # return memo[0][0]

        res = float('-inf')

        curr = 0

        l, r = 0, 0

        while r < len(nums):
            curr += nums[r]
            res = max(res, curr)
            if r < len(nums) - 1 and curr < 0:
                l = r + 1
                curr = 0
            r += 1  
        return res



