from heapq import heappop, heappush


def maxScore(nums1, nums2, k):
    total = res = 0
    heap = []
    
    pairs = zip(nums1, nums2)
    print(pairs)
    sorted_pairs = sorted(pairs, key=lambda x: -x[1])
    print(sorted_pairs)
    for pair in sorted_pairs:
        num1, num2 = pair
        print(num1, num2)
        heappush(heap, num1)
        print(heap)
        total += num1
        if len(heap) > k:
            total -= heappop(heap)
            print(heap, total)
        if len(heap) == k:
            res = max(res, total * num2)
            print(num2)
            print(total * num2)
            print(res)
    
    return res

def main():
    nums1 = [1,2,1,4]
    nums2 = [2,1,3,4]
    k = 2
    print(maxScore(nums1, nums2, k))

if __name__ == '__main__':
    main()  # Call the main function