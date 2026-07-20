class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        res = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-min_price
            min_price = min(prices[i],min_price)
            res = max(res, profit)
        
        return res