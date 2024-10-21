class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.sumDigits(n)
        return True
    
    def sumDigits(self, n: int) -> int:
        sum = 0
        while n !=0:
            sum += (n % 10)**2
            n //= 10
        return sum