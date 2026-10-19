class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for i in range(1, max(piles)):
        #     temp = h
        #     for j in range(0, len(piles)): 
        #         temp -= math.ceil(piles[j] / i)
        #     if temp >= 0:
        #         return i
        # return max(piles)
        l, r = 0, max(piles)
        res = max(piles)
        while l <= r:
            mid = l + (r - l) // 2
            if mid == 0:
                return res
            temp = h
            for i in range(len(piles)):
                temp -= math.ceil(piles[i] / mid)
            if temp >= 0:
                res = min(res, mid)
                r = mid - 1
            elif temp < 0:
                l = mid + 1
            else:
                r = mid - 1

        return res