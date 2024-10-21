from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        r = 1
        while r < len(chars):
            if chars[r] != chars[l]:
                if r - l > 1:
                    cnt = str(r-l)
                    for i, c in enumerate(cnt):
                        chars[l+i+1] = str(c)
                    l = l + len(c) + 1
                    chars = chars[:l] + chars[r:]
                    r = l + 1
                else:
                    l = l + 1
                    chars = chars[:l] + chars[r:]
                    r = l + 1
            else:
                r += 1
                if r == (len(chars)):
                    cnt = str(r-l)
                    for i, c in enumerate(cnt):
                        chars[l+i+1] = str(c)
                    l = l + len(cnt) + 1
                    chars = chars[:l]
        print(chars)
        return len(chars)
Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])