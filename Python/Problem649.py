from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        res = deque()
        i = 0
        while len(senate) > 1:
            if not res or res[0] == senate[i]:
                res.append(senate[i])
                i += 1
            else:
                res.popleft()
                senate = senate[:i] + senate[i+1:]
            if len(senate) == len(res):
                break
            if i == len(senate):
                i = 0
        return "Radiant" if senate[0] == "R" else "Dire"
print(Solution().predictPartyVictory("RRR"))