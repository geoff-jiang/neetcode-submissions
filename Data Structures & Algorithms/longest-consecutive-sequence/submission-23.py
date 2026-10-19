class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)

        if len(nums) == 0:
            return 0

        res = 0
        temp = 1
        for i in range(1, len(nums)):
            
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                temp += 1
            else:
                res = max(res,temp)
                temp = 1
                
        return max(res, temp)
            