class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result * 2 + (n % 2)
            n = n // 2
        return result
    def reverseBitsShifting(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
    def reverseBitsSwap(self, n: int) -> int:
        print(bin(n))
        n = ((n & 0b11111111111111110000000000000000) >> 16) | ((n & 0b00000000000000001111111111111111) << 16)
        print(bin(n & 0b11111111111111110000000000000000), bin(n & 0b00000000000000001111111111111111))
        n = ((n & 0b11111111000000001111111100000000) >> 8)  | ((n & 0b00000000111111110000000011111111) << 8)
        print(bin(n & 0b11111111000000001111111100000000), bin(n & 0b00000000111111110000000011111111))
        n = ((n & 0b11110000111100001111000011110000) >> 4)  | ((n & 0b00001111000011110000111100001111) << 4)
        n = ((n & 0b11001100110011001100110011001100) >> 2)  | ((n & 0b00110011001100110011001100110011) << 2)
        n = ((n & 0b10101010101010101010101010101010) >> 1)  | ((n & 0b01010101010101010101010101010101) << 1)
        return n

result = Solution().reverseBitsSwap(43261596)
print(result) # 964176192