def selection_sort(arr):
    n = len(arr)
    #NOTE: this has time complexity of O(n^2).
    #NOTE: selects the mini element and puts it into the right spot.
    #NOTE: the outer loop goes till n-2 only.
    for i in range(n - 1):
        mini = i 
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]

arr = [5,3,3,6,2,8,1]
selection_sort(arr)
print("The array after sorting: ")
print(*arr)
#NOTE: the * operator is called splat or the unpacking operator is used to unpack the elements of the list.
