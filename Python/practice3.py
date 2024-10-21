def main():
    ransomNote = input("ransomNote \n")
    magazine = input("magazine \n")
    check = compare(ransomNote,magazine)
    print(check)

def compare(ransomNote,magazine):
    t = 0
    for i in magazine:
        if i == ransomNote[t]:
            print(ransomNote[t])
            print(t)
            t += 1
        else:
            t = 0

        if t > len(ransomNote) -1:
            return True
    return False   

if __name__ =='__main__':
    main()