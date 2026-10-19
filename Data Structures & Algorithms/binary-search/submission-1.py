class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1
        mid = r // 2
        while l <= r:   
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
                mid = l + (r - l) // 2
            else:
                r = mid - 1
                mid = l + (r - l) // 2
        return -1

        