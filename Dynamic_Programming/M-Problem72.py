class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        dp = [[0]*len2 for _ in range(len1)]

        for i in range(len1):
            dp[i][0] = i
        for j in range(len2):
            dp[0][j] = j

        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]
    
    def minDistance2(self, word1: str, word2: str) -> int:
        prev = [i for i in range(len(word2)+1)]

        for i in range(1, len(word1) + 1):
            curr = [0] * (len(word2) + 1)
            curr[0] = i
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j-1], prev[j], curr[j-1])
            prev = curr
        
        return prev[len(word2)]

    def minDistance3(self, word1: str, word2: str) -> int:
        curr = [i for i in range(len(word2)+1)]
        for i in range(1, len(word1) + 1):
            prev = curr[:]
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j-1], prev[j], curr[j-1])
        return curr[-1]
                

Solution().minDistance3("horse", "ros")