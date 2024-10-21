class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s = list(s)
        l, r = 0, len(s)-1

        while r > l:
            if s[r] in vowels and s[l] in vowels:
                s[r], s[l] = s[l], s[r]
                r -= 1
                l += 1
            if s[r] not in vowels:
                r -= 1
            if s[l] not in vowels:
                l += 1
        return ''.join(s)
    
result = Solution().reverseVowels("a a")
print(result)