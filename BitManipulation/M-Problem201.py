class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        nums_of_zero_on_right = 0
        while left != right:
            left >>= 1
            right >>= 1
            nums_of_zero_on_right += 1
        return left << nums_of_zero_on_right
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right