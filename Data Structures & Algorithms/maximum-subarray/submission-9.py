class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        memo = [[0] * 2 for _ in range(n)]

        memo[n-1][1], memo[n-1][0] = nums[n-1], nums[n-1]

        for i in range(n-2, -1, -1):
            memo[i][1] = max(nums[i] + memo[i + 1][1], nums[i])
            memo[i][0] = max(memo[i][1], memo[i + 1][0])
        
        return memo[0][0]



