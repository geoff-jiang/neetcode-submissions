class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        res = 0

        for i, v in enumerate(nums):
            if i >= 1:    
                maxSoFar = 0
                for j in range(i - 1, -1, -1):
                    if nums[j] < v:
                        maxSoFar = max(maxSoFar, 1 + dp[j])
                        dp[i] = maxSoFar
        return max(dp)

            