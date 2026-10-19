class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = [1] * n
        curr = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = curr
            curr *= nums[i]
        back = 1
        res= []
        for i in range(0, len(nums), 1):
            res.append(back * suffix[i])
            back *= nums[i]
        return res
            
        #[1, 2, 4, 6]
        #expecting [48, 24, 6, 1]

