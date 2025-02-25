class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: -x[1])
        merged = []
        for interval in intervals:
            if not merged or interval[1] < merged[-1][0]:
                merged.append(interval)
            else:
                merged[-1][0] = min(merged[-1][0], interval[0])
        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]
            
            if curr[0] <= prev[1]:  # Overlapping intervals
                prev[1] = max(prev[1], curr[1])  # Merge
            else:
                merged.append(curr)
        
        return merged