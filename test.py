def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    length = 0
    for r in range(len(s)):
        char = s[r]
        if char in seen and seen[char] >= l:
            print(char, seen, seen[char])
            l = seen[char] + 1
            print(l)
        else:
            length = max(length, r - l + 1)
        seen[char] = r

    return length

def main():
    in_string = input()  # Take user input
    lengthOfLongestSubstring(in_string)  # Call the lookup function with the input string

if __name__ == '__main__':
    main()  # Call the main function