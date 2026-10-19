class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        counter = 0
        while r < len(nums) - 1:
            temp = 0
            for i in range(l, r + 1):
                temp = max(temp, i + nums[i])
            l = r + 1
            r = temp
            counter += 1

        return counter