def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

def order_weight(strng):
    #print(strng.split())
    return strng.split()
    '''
    print(lst)
    print(1)
    #now the "bubble sort"
    bubble_sort(lst)
    print(lst)
    print(2)
    
    # your code
'''
#print(order_weight([103,123,4444,99,2000]))
print(bubble_sort([103,123,4444,99,2000]))


str=order_weight("103 123 4444 99 2000")
print(str)
print(bubble_sort(str))
#("103 123 4444 99 2000") -> "2000 103 123 4444 99")
    
#("2000 10003 1234000 44444444 9999 11 11 22 123")
#-> "11 11 2000 10003 22 123 1234000 44444444 9999")
