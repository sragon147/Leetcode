class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = 0
        x = str(x)
        r = len(x) - 1
        while l < r:
            if x[l] != x[r]:
                return False
            l = l + 1
            r = r - 1
        return True