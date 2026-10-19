class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix, suffix arrays
        # 2 pointers
        
        n = len(height)
        # prefix = [0] * n
        # suffix = [0] * n
        # # tallest wall up to that point

        # prefix[0] = height[0]
        # for i in range(1, n):
        #     prefix[i] = max(prefix[i-1], height[i])         
        # suffix[n-1] = height[-1]
        # for i in range(n-2,-1, -1):
        #     suffix[i] = max(suffix[i + 1], height[i])  
        # total = 0
        # for i in range(n):
        #     total += min(suffix[i], prefix[i]) - height[i]
        # return total

        l, r = 0, n - 1
        maxL, maxR = height[0], height[-1]
        total = 0 
        while l < r: 
            if maxL < maxR: 
                l += 1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]
        return total
        
        

        

