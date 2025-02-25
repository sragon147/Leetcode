class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n < 0:
            x = 1/x
            n = -n
        while n != 0:
            res = self.myPow(x, n//2)
            if n % 2 == 0:
                return  res * res
            else:
                return res * res * self.myPow(x, 1)
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        pow = 1
        while n != 0:
            if (n&1 == 1):
                pow *= x
            
            x *= x
            n >>= 1
        return pow

Solution().myPow(2.00000, 10)