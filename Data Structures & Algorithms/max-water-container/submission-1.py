class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxFound = 0
        for i, v in enumerate(heights):
            pos, curr = i, v
            counter = i + 1 
            while counter < len(heights):
                diff = counter - pos
                currMax = diff * min(heights[counter], curr)
                if currMax > maxFound:
                    maxFound = currMax
                counter += 1
        return maxFound