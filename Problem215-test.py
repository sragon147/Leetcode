def partition(nums, left, right):
    pivot = nums[left]
    l, r = left + 1, right

    while l <= r:
        # If both pointers are valid and nums[l] < pivot, nums[r] > pivot, swap them
        print(f"before: {nums}")
        if nums[l] < pivot and nums[r] > pivot:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        # If nums[l] is in the correct position (>= pivot), move left pointer
        if nums[l] >= pivot:
            l += 1
        # If nums[r] is in the correct position (<= pivot), move right pointer
        if nums[r] <= pivot:
            r -= 1
        print(f"after: {nums}")
        print(l, r)

    # Place the pivot in its correct position
    nums[left], nums[r] = nums[r], nums[left]
    return r


# Test the function
def test_partition():
    nums = [6, 3, 8, 5, 2, 7, 4, 1, 9]
    pivot_index = partition(nums, 0, len(nums) - 1)
    print(f"Pivot index: {pivot_index}")
    print(f"Partitioned array: {nums}")


# Run the test
test_partition()
