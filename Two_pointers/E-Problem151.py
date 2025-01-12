class Solution:
    def reverseWords(self, s: str) -> str:
        l = r = len(s) - 1
        res = ''
        while l >= -1:
            if r == l:
              if s[l] == ' ':
                r -= 1
                l -= 1
                continue
              else:
                l -= 1
                continue
            else:
              if s[l] == ' ' or l == -1:
                res += s[l+1:r+1] + ' '
                r = l-1
              l -= 1
        return res.strip()
    
result = Solution().reverseWords("F R  I   E    N     D      S      ")
print("\"", result, "\"")