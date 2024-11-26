class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU"
        current_vowels = 0
        max_vowels = 0

        for i in s[:k]:
            if i in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        for i in range(k , len(s)):

            if s[i - k] in vowels:
                current_vowels -= 1

            if s[i] in vowels:
                current_vowels += 1
                max_vowels = max(max_vowels , current_vowels)

        
        return max_vowels

print(Solution().maxVowels("weallloveyou", 7)) # 3
                