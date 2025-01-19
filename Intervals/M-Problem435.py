from typing import List
class Solution:
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c = 0
        prev_r = -float("inf")
        for l, r in intervals:
            print(l, r, prev_r, c)
            if l < prev_r:
                c += 1
                if r < prev_r:
                    prev_r = r
                continue            
            prev_r = r
        return c
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_end, count = float('-inf'), 0
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if min_end <= start:
                min_end = end
                count += 1
        return len(intervals) - count

Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])