class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        toEnd = [1] * len(nums)
        toStart = [1] * len(nums)
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            toEnd[i] = cur
            cur *= nums[i]
        res = []
        cur = 1
        for i in range(len(nums)):
            toStart[i] = cur 
            cur *= nums[i]
            res.append(toStart[i] * toEnd[i])
        return res



