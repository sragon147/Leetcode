class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        while a != 0 or b !=0 or c != 0:
            lb_a = a & 1
            lb_b = b & 1
            lb_c = c & 1 
            if lb_a | lb_b != lb_c:
                if lb_a == lb_b == 1:
                    count += 2
                else:
                    count += 1 
            a >>= 1
            b >>= 1
            c >>= 1
        return count
Solution().minFlips(8, 3, 5)
# 1000
# 0011
# 0101

# 010
# 110
# 101