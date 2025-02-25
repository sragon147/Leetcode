from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(remain, path, start):
            if remain == 0:
                res.append(path.copy())
                return
            
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtracking(remain - candidates[i], path, i)
                path.pop()

        backtracking(target, [], 0)
        return res
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        tmp = []
        ans = []
        candidates.sort()
        self.backtracking(candidates, target, tmp, ans)

        return ans
    
    def backtracking(self, candidates, target, tmp, ans):
        for i in range(len(candidates)):
            if candidates[i] == target:
                tmp.append(candidates[i])
                ans.append(tmp[:])
                tmp.pop()
                return 
            elif candidates[i] > target:
                return
            else:
                tmp.append(candidates[i])
                self.backtracking(candidates[i:], target-candidates[i], tmp, ans)
                tmp.pop()
Solution().combinationSum([2,3,6,7], 7)