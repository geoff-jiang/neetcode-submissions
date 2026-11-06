class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix_sum
            prefix_sum *= nums[i]
           
        suffix_sum = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix_sum
            suffix_sum *= nums[i]

        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = prefix[i] * suffix[i]
        
        return res

        