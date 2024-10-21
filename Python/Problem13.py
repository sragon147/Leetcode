roman = {"I" : 1,
         "V" : 5,
         "X" : 10,
         "L" : 50,
         "C" : 100,
         "D" : 500,
         "M" : 1000}

def convert_to_arbic(s):
    value = 0
    temp = "M"
    for i in s:
        if roman[i] > roman[temp]:
            value -= 2*roman[temp]
            value += roman[i]
        print(value)
        temp = i

def main():
    inRoman = input()
    convert_to_arbic(inRoman)

if __name__ =='__main__':
    main()
