# List[List[int]]
def Grouping(List):
    while(len(List)>0):
        notGrouped = []
        group = List[0]
        index = 0
        
        for i in List:
            if i == group:
                index += 1
            else:
                notGrouped.append(i)
        
        List = notGrouped
        print(group,index)
        print(List)

def main():
    Grouping([[1,2,3],[0,2],[0,1,3],[0,2]])  #Grouping the input to multiple group

if __name__ == '__main__':
    main()  # Call the main function