def kthelement(arr1, arr2, m, n, k):
    if m > n:
        kthelement(arr2, arr1, n, m, k) 

    low = max(0, k - m)
    high = min(k, n)

    while low <= high:
        cut1 = (low + high) >> 1 
        cut2 = k - cut1 
        l1 = MIN_VALUE if cut1 == 0 else arr1[cut1 - 1] 
        l2 = MIN_VALUE if cut2 == 0 else arr2[cut2 - 1]
        r1 = MAX_VALUE if cut1 == n else arr1[cut1]
        r2 = MAX_VALUE if cut2 == m else arr2[cut2] 
        
        if l1 <= r2 and l2 <= r1:
            print(cut1, cut2)
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1

from typing import List
import bisect

def query_k_min(vecs: List[List[int]], k: int) -> int:
    # we assume each number >=1 and <=10^9
    l, r = 0, 10**9
    while r - l > 1:
        m = (l+r)>>1
        tot = 0
        for vec in vecs:
            tot += bisect.bisect_right(vec, m)
        if tot >= k: r = m
        else: l = m
    return r

a = [[2,3,6,7,11],[1,4,9,10],[2,3,5,7]]
for x in range(1,14):
    print(query_k_min(a,x))

def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]
    
    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)