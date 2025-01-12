from heapq import heappop, heappush

class Solution:
    def maxScore(self, A, B, k):
        total = res = 0
        h = []
        # Pair elements from lists A and B
        paired_list = list(zip(A, B))

        # Sort the paired list by the second element (from B) in descending order
        sorted_pairs = sorted(paired_list, key=lambda pair: pair[1], reverse=True)
        print(sorted_pairs)
        # Iterate over the sorted pairs
        for a, b in sorted_pairs:
        # for a,b in sorted(list(zip(A, B)), key=lambda ab: -ab[1]):                
            heappush(h, a)
            total += a
            if len(h) == k:
                print(res, total, b)
                res = max(res, total * b)
                total -= heappop(h)
        return res

Solution().maxScore([4,2,3,1,1], [7,5,10,9,6], 3)