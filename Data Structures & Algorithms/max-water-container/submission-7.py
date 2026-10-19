class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxFound = 0
        while l < r:
            temp = (r - l) * min(heights[l], heights[r])
            maxFound = max(temp, maxFound)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r-=1
        return maxFound