def find_even_index(arr):
    ind=0
    for i in range(len(arr)):
        sumLeft=abs(sum(arr[:i]))
        sumRight=abs(sum(arr[i+1:]))
        if sumLeft==sumRight:
            ind=i
            break
    return ind if abs(sum(arr[:ind]))== abs(sum(arr[ind+1:])) else -1

array=[1,2,3,4,3,2,1]
array1=[-1,-2,-3,-4,-3,-2,-1]
array2=[20,10,-80,10,10,15,35]
array3=[10,-80,10,10,15,35,20]

print("array: ",find_even_index(array),"\n")
print("array1: ",find_even_index(array1),"\n")
print("array2: ",find_even_index(array2),"\n")
print("array3: ",find_even_index(array3),"\n")
