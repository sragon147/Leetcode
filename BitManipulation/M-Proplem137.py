class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            s = 0
            mask = 1 << i
            for num in nums:
                s += (num & mask)
            if s % 3:
                res |= mask
        # If signed bit is set then adjust the number
        if res & 1 << 31:
            res -= 2 ** 32
        return res

    def singleNumber(self, nums: List[int]) -> int:
        x1, x2, mask = 0, 0, 0
        for num in nums:
            x2 ^= x1 & num
            x1 ^= num
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask
        return x1
    
    def singleNumber(self, nums: List[int]) -> int:
        x1, x2 = 0, 0
        for num in nums:
            x1 = (x1 ^ num) & ~x2
            x2 = (x2 ^ num) & ~x1
        return x1
