import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(array, k):
            pivot = random.choice(array)
            left,right,mid = [],[],[]

            for num in array:
                if num < pivot:
                    left.append(num)
                elif num > pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if len(right) >= k:
                return quick_select(right,k)
            elif k > len(right) + len(mid):
                return quick_select(left,k - len(right) - len(mid))
            else:
                return pivot
            
        return quick_select(nums,k)