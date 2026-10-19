class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = len(nums)-1
            while (j > i):
                if nums[i] == target - nums[j]:
                    return [i, j]
                else:
                    j = j- 1
        return []