def lookup(string):
    ref = string[0]  # Initialize reference character with the first character of the string
    res = 0  # Initialize the result to 0 (length of longest consecutive sequence)
    
    for s in string:  # Iterate over each character in the string
        for i in ref:  # Iterate over the reference character(s)
            if s == i:  # If the character is equal to the reference character
                ref = s  # Update the reference character
                break  # Exit the inner loop
            
        else:  # This block is executed when the inner loop completes without a break
            ref += s  # Append the character to the reference character(s)
            if res < len(ref):  # If the length of the reference characters is greater than the result
                res = len(ref)  # Update the result to the length of the reference characters
        
        print(ref, res)  # Print the current reference characters and result
    
def main():
    in_string = input()  # Take user input
    lookup(in_string)  # Call the lookup function with the input string

if __name__ == '__main__':
    main()  # Call the main function