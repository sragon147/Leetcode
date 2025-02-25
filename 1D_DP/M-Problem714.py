from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = [[0]*2 for _ in range(len(prices))]
        profit[0][0] = -prices[0]
        for i in range(1, len(prices)):
            profit[i][0] =max((profit[i-1][1] - prices[i]), profit[i-1][0])
            profit[i][1] = max((profit[i-1][0] + prices[i] - fee), profit[i-1][1])
        return profit[len(prices)-1][1]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0
        for p in prices:
            new_hold = max(hold,cash - p)
            new_cash = max(cash,hold + p - fee)
            hold,cash = new_hold,new_cash
        return cash

Solution().maxProfit([4,5,2,4,3,3,1,2,5,4], 1)