class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        result = 0

        for i in range(1,len(prices)):
            profit = prices[i] - min_price
            min_price = min(min_price,prices[i])
            result = max(profit,result)

        return result