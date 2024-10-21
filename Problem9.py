def reverse(s):
    front_end_point = len(s)// 2
    back_start_point = front_end_point + (len(s) % 2) - 1
    i = len(s)-1
    obverse_s = s [:front_end_point]
    reverse_s = ""
    while(i > back_start_point):
        reverse_s += str(s[i])
        i -= 1
    return [obverse_s,reverse_s] 

def compare(s):
    compare_s = reverse(s)
    if compare_s[0] == compare_s[1]:
        return True
    else:
        return False

def main():
    target = input()
    check = compare(target)
    if check == True:
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ =='__main__':
    main()