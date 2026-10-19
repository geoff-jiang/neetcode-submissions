class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxFromStart = []
        maxFromEnd = []
        stemp = 0
        for h in height:
            maxFromStart.append(stemp)
            stemp = max(stemp, h)
        etemp = 0
        for l in range(len(height) - 1, -1, -1):
            maxFromEnd.append(etemp)
            etemp = max(etemp, height[l])
        maxFromEnd.reverse()

        print(maxFromStart)
        print(maxFromEnd)
        
        res = 0
        for i, v in enumerate(height):
            if (maxFromStart[i] != 0 and 
            maxFromEnd[i] != 0 and 
            v < maxFromStart[i] and 
            v < maxFromEnd[i]):
                res += min(maxFromStart[i], maxFromEnd[i]) - v
        return res

