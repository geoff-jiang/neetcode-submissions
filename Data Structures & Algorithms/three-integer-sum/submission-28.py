class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        sorted_nums = sorted(nums)
        l = 0
        r = len(sorted_nums) - 1
        res = []
        for i, v in enumerate(sorted_nums):
            prev = sorted_nums[i-1]
            if i >= 1 and v == prev: 
                continue
            target = v * -1
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                temp = sorted_nums[l] + sorted_nums[r]
                if temp == target:
                    res.append([v, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r :
                        l+=1
                elif temp < target:
                    l += 1 
                else:
                    r-=1
        return res
            

                