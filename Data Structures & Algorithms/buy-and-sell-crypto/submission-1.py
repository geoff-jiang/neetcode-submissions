class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices: 
            res = max(res, price - lowest)
            lowest = min(lowest, price)
        return res