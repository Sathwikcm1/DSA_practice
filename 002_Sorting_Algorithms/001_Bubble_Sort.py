#FIXME: Bubble sort, repeatedly steps through the list, compares the adjancent elements and swaps them if they are in the wrong order. 
#Time complexity: Worst : O(N^2) and O(n^2) as average and O(N) as the best case.
def bubble_sort(arr):

    #TODO: bubble sort, bubbling up the largest element in the array to the end of the array.

    n = len(arr)
    for i in range(n):
        #TODO: the inner loop don't have to go till n-1 because the last elements will already be sorted.
        #NOTE: i is given here, because it will be coming from the end, no if we are subtracting i from n.
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("This is using bubble sort:")
    for num in arr:
        print(num, end=" ")
    print()

arr = [5,4,3,3,6,2,8,1]
bubble_sort(arr)
