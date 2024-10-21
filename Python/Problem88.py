from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m+n
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n-1]:
                nums1[k - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[k - 1] = nums2[n - 1]
                n -= 1
            k -= 1
        print(nums1)

solution = Solution()
nums1 = [9, 10, 23, 0, 0, 0, 0, 0, 0]
m = 3
nums2 = [1, 3, 4, 18, 20, 21]
n = 6
solution.merge(nums1, m, nums2, n)
print(nums1)