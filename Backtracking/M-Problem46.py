from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in visited:
                    continue
                path.append(num)
                visited.add(num)
                backtrack(path, visited)
                path.pop()
                visited.remove(num)
        
        backtrack([], set())
        return res
    
    from typing import List

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index):
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(0)
        return res

    def recursive(nums):
        from collections import deque
        q = deque()
        q.append((nums, []))
        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path+[nums[i]]))
        return res


Solution().permute([1,2,3])