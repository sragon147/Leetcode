class Solution:
    def tribonacci(self, n: int) -> int:
        mem_1, mem_2, mem_3 = 0, 1, 1
        if n == 0:
            return mem_1
        if n == 1:
            return mem_2
        if n == 2:
            return mem_3
        res = 0
        for _ in range(3, n+1):
            res = mem_1 + mem_2 + mem_3
            mem_1, mem_2, mem_3 = mem_2, mem_3, res
            print(mem_1, mem_2, mem_3, res)
        return res

Solution().tribonacci(4)