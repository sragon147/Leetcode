class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        for i in range(len(s)):
            if s[i] in map_s:
              if map_s[s[i]] != t[i]:
                return False
              else:
                continue
            map_s[s[i]] = t[i]
        return True
result = Solution().isIsomorphic("egg", "add")