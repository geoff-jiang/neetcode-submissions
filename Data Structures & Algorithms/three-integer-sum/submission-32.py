class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        for i, v in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            target = v * -1
            l, r = i + 1, len(sorted_nums) - 1
            while l < r:
                s = sorted_nums[l] + sorted_nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([v, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1 
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l+=1
        return res
        
            

                