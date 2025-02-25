from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(amount, memo):
            if amount == 0:
                return 0
            
            if amount in memo:
                return memo[amount]
            
            min_count = amount + 1
            for coin in coins:
                if coin <= amount:
                    result = helper(amount - coin, memo)
                    if result != -1:
                        min_count = min(min_count, result + 1)
            
            memo[amount] = -1 if min_count == amount + 1 else min_count
            return memo[amount]
        
        return helper(amount, {})

    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:  
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1

Solution().coinChange([1,2,5], 11)
