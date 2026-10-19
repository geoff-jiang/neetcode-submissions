class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        count = 0
        while l < r:
            count = min(heights[l], heights[r]) * (r - l)
            print(count)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            res = max(count, res)
        return res