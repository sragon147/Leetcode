class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2: return n
        filled_prev, gap_prev, filled_prev2, gap_prev2 = 2,2,1,1
        for i in range(3, n+1):
            filled = filled_prev + filled_prev2 + 2*gap_prev2
            gap = filled_prev + gap_prev
            
            filled_prev2, filled_prev, gap_prev2, gap_prev = filled_prev, filled, gap_prev, gap
        return filled_prev % 1_000_000_007
    
    def numTilings(self, n: int) -> int:
        v = [0] * len(n)
        v[0] = 1
        if n == 1:
            return v[0]
        v[1] = 2
        if n == 2:
            return v[1]
        v[2] = 5
        if n == 3:
            return v[2]
        for i in range(n):
            v[i] = 2*v[i-1] + v[i-3]
            v[i] % 1_000_000_007
        return v[n-1]