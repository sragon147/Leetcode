def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            print(temp,i)
            j = i
            while j >= interval and array[j - interval] > temp:
                print(array[j],array[j - interval],j)
                array[j] = array[j - interval]
                j -= interval
                print(array[j],j)
            print()

            array[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
shellSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)