class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            while i % 5 == 0:
                count += 1
                i //= 5
        return count
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
Solution().trailingZeroes(5)