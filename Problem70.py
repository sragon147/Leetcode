class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        one_step_away, two_step_away = 1, 1
        for i in range(2, n+1):
            curr = one_step_away + two_step_away
            two_step_away = one_step_away
            one_step_away = curr
        return curr
    
result = Solution().climbStairs(5)
print(result) # 3