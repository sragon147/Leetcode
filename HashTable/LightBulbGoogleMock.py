from typing import List
class Solution:
    def tougleRangeOfLightBulb(K: int, flips: List[tuple[int, int]]) -> int:
        mapped = []
        for flip in flips:
            mapped.append([flip[0], 1])
            mapped.append([flip[1], -1])
        mapped.sort()
        counter = 0
        total_time_on = 0
        last_time = None

        for time, change in mapped:
            if counter % 2 == 1:
                total_time_on += time - last_time

            counter += change
            last_time = time
            print(time, counter, total_time_on)

        return total_time_on

Solution.tougleRangeOfLightBulb(5000, [(2000, 3000), (1000, 3500), (2000,2500), (3000,4500)])