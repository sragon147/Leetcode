def lookup(string):
    left_pointer = 0
    right_pointer = 1
    longest_string = string[left_pointer]
    length = 0

    while right_pointer < len(string):
        if string[right_pointer] in longest_string:
            left_pointer = right_pointer - (len(longest_string)-int(longest_string.index(string[right_pointer]))-1)
            right_pointer = left_pointer
            longest_string = string[left_pointer]
        else:
            longest_string += string[right_pointer]
            length = max(length, right_pointer - left_pointer + 1)
            print(left_pointer, right_pointer, length)
        
        right_pointer += 1
    
    return length

def main():
    in_string = input()  # Take user input
    lookup(in_string)  # Call the lookup function with the input string

if __name__ == '__main__':
    main()  # Call the main function