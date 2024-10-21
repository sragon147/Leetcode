def Closest(nums, target):
    nums.sort()
    print(nums)
    closest = []
    for i in range(len(nums)-3):
        r = len(nums)-1
        l = i+1
        while(l < r):
            total = nums[i]+nums[l]+nums[r]
            closest.append(total-target)
            print(l,r,total)
            if total == target:
                return total
            elif total < target:
                l += 1
            else: r -= 1
        print(closest)


def main():
    nums = [-1,2,1,-4,-3,5,2,0,-1,9,7]
    target = 2.5

    Closest(nums, target)

if __name__ == '__main__':
    main()  # Call the main function