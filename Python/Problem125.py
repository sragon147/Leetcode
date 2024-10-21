class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        s =s.lower()
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] not in alphabet:
                left += 1
                continue
            if s[right] not in alphabet:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

print(Solution.isPalindrome('A man, a plan, a canal: Panama'))