from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def searchStart(target) -> int:
            l, r = 0, len(intervals) - 1
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid][0] == target:
                    return mid
                elif intervals[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        def searchEnd(target) -> int:
            l, r = 0, len(intervals) - 1
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid][1] == target:
                    return mid
                elif intervals[mid][1] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        
        start = searchStart(newInterval[0])
        end = searchEnd(newInterval[1])
        
        if len(intervals) == 0:
            return [newInterval]
        print(start, end)
        res = []
        if start > 0:
            res = intervals[0:start-1]
            if intervals[start -1][1] >= newInterval[0]:
                newInterval[0] = min(intervals[start -1][0], newInterval[0])
            else:
                res.append(intervals[start -1])
        if end < len(intervals) -1:
            if intervals[end + 1][0] <= newInterval[1]:
                newInterval[1] = max(intervals[end + 1][1], newInterval[1])
            else:
                return res + [newInterval] + intervals[end + 1:]
        return res + [newInterval] + intervals[end + 2:]
    def insert2(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left, right = [], []
        for i in intervals:
            if i.end < s:
                left += i,
            elif i.start > e:
                right += i,
            else:
                s = min(s, i.start)
                e = max(e, i.end)
        return left + [Interval(s, e)] + right
print(Solution().insert([[1,3],[6,9]], [2,5]))