class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointers
        # store max left wall and max right wall encountered
        # take mininmum - current value. 
        # if left <= right, move left pointer. otherwise move right
        
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        res = 0

        while l < r:
            
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                res += max(0, min(max_left, max_right) - height[l])
            else:
                r -= 1
                max_right = max(max_right, height[r])
                res += max(0, min(max_left, max_right) - height[r])
        return res
