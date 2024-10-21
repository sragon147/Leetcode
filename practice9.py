def MaxArea(height):
    r_pointer = len(height)-1
    l_pointer = 0
    high = 0
    while (l_pointer != r_pointer):
        if height[l_pointer] < height[r_pointer]:
            high = max(high, height[l_pointer]*(r_pointer-l_pointer))
            l_pointer = l_pointer + 1
            print(high, l_pointer)

        else:
            high = max(high, height[r_pointer]*(r_pointer-l_pointer))
            r_pointer = r_pointer - 1
            print(high, r_pointer)

def main():
    height = [1,6,9,2,5,4,8,7,3]

    MaxArea(height)

if __name__ == '__main__':
    main()  # Call the main function