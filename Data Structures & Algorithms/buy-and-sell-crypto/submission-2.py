class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        res = 0
        
        while r != len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                temp = prices[r] - prices[l]
                res = max(res, temp)

            r += 1
        return res