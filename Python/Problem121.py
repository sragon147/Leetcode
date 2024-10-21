from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 - prices[0]
        profit = 0
        for i in range(1, len(prices)):
            sale = buy + prices[i]
            if sale < 0:
                buy = 0 - prices[i]
            if sale > profit:
                profit = sale
        return profit
    
result = Solution().maxProfit([7,1,5,3,6,4])
print(result) # 5