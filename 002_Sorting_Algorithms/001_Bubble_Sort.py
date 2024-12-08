def bubble_sort(arr):
    #TODO: bubble sort, bubbling up the largest element in the array to the end of the array.
    
    n = len(arr)
    for i in range(n):
        #TODO: the inner loop don't have to go till n-1 because the last elements will already be sorted.
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("This is using bubble sort:")
    for num in arr:
        print(num, end=" ")

arr = [5,4,3,3,6,2,8,1]
bubble_sort(arr)
#mew.
