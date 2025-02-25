class Solution:
    def isPowerOfTwoAndOperator(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    
    def isPowerOfTwoCountNumberOfBit1(self, n: int) -> bool:
        if n <= 0:
            return False
        cnt = bin(n).count('1')
        return cnt == 1