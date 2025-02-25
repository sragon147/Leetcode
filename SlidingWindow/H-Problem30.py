from collections import defaultdict
from typing import Counter, List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        res = []
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1
        dict_copy = dict.copy()
        for i in range(n):
            l = r = i
            dict = dict_copy.copy()
            while r < len(s) - i:
                if s[r:r+n] in words:
                    if dict[s[r:r+n]] > 0:
                        dict[s[r:r+n]] -= 1
                        if sum(dict.values()) == 0:
                            res.append(l)
                            dict[s[l:l+n]] += 1
                            l += n
                        r += n
                    else:
                        while s[l:l+n] != s[r:r+n]:
                            dict[s[l:l+n]] += 1
                            l += n
                        l += n
                        r += n
                else:
                    r += n
                    l = r
                    dict = dict_copy.copy()
        return res
    
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        wordsCount = Counter(words)
        n, wordLen = len(s), len(words[0])
        totalLen = wordLen * len(words)
        ans = []

        # we need to traverse s worldLen times
        for i in range(wordLen):
            curCount = defaultdict(int)

            # tarverse s with diff beginning index
            for j in range(i, n-wordLen+1, wordLen):

                # hashing a worldLen len string
                if s[j:j+wordLen] in wordsCount:
                    curCount[s[j:j+wordLen]] += 1

                # subtract a worldLen len string if the string in words
                if j >= totalLen and s[j-totalLen: j-totalLen+wordLen] in wordsCount:
                    curCount[s[j-totalLen: j-totalLen+wordLen]] -= 1

                if curCount == wordsCount:
                    ans.append(j-totalLen+wordLen)
        return ans
Solution().findSubstring("barfoothefoobarman", ["foo","bar"]) 
