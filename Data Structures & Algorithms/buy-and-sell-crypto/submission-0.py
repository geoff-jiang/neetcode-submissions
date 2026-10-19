class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i, v in enumerate(prices): 
            j = i + 1
            while j < len(prices):
                if prices[j] - v > res:
                    res = prices[j] - v
                j += 1
        return res