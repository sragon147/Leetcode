class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        tar = str2
        if tar not in str1:
            return ''
        while len(str1) % len(tar) !=0 or len(str2) % len(tar) !=0:
            tar = tar[:len(tar)-1]
        return tar

result = Solution().gcdOfStrings("ABABAB", "ABAB")
print(result)
            