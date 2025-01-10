#FIXME: The problem is to rotate the whole array by one place, for example:  
#array = [1,2,3,4,5], rotated array by one place: [2,3,4,5,1]

#TODO: brute force solution: we can just use another array to copy the first part and add the first element to the last.
def brute_force(arr):
    n = len(arr)
    first_e = arr[0]
    temp = []
    j = 0
    for i in range(1,n):
        temp.append(arr[i])
        j += 1
    for i in range(len(temp)):
        arr[i] = temp[i]
    arr[n-1] = first_e
#NOTE: this will take the time complexity of O(n).

#TODO: copy the first element to a variable and then move all the elements to one place behind, at the end add the first element.

def optimal(arr):
    n = len(arr)
    first_e = arr[0]
    for i in range(1,n):
        arr[i - 1] = arr[i]
    arr[n-1] = first_e

arr = [1,2,3,4,5]
optimal(arr)
print(arr)
#NOTE: The time complexity of optimal is O(N.) single iteration.
