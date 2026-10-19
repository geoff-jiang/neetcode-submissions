class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixForwards = [1] * len(nums)
        prefixBackwards = [1] * len(nums)

        total = 1
        for i in range(1, len(nums)):
            total *= nums[i - 1]
            prefixForwards[i] = total
        
        total = 1
        for i in range(len(nums) - 2, -1, -1):
            total *= nums[i + 1]
            prefixBackwards[i] = total
        
        res = []
        prefixForwards[0] = prefixBackwards[-1] = 1
        for i in range(len(nums)): 
            res.append(prefixForwards[i] * prefixBackwards[i])
        
        return res

        