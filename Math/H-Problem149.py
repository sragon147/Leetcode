from collections import defaultdict
import math
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return abs(a)
        
        if len(points) <= 1:
            return len(points)
        
        max_points = 1
        
        for i in range(len(points)):
            line_map = defaultdict(int)
            local_max = 0
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                a = points[j][0] - points[i][0]
                b = points[j][1] - points[i][1]
                
                gcd_value = gcd(a, b)  # Using the manual gcd function
                a //= gcd_value
                b //= gcd_value
                
                # Normalize the vector
                if a < 0:
                    a, b = -a, -b  # Ensure a is positive
                elif a == 0:  
                    b = abs(b)  # Ensure b is positive for vertical lines
                
                vector = (a, b)
                line_map[vector] += 1
                local_max = max(local_max, line_map[vector])
            
            max_points = max(max_points, local_max + 1)  # Include the current point
        
        return max_points
