#FIXME: insertion_sort basically builds a sorted array one element at a time by repeatedly taking the next element from the unsorted potion and inserting it into the right position.
#Time complexity: O(n) best case, O(n^2) for both remaining.
def insertion_sort(arr):
    n = len(arr)
    #NOTE: goes from 1 to n-1.
    for i in range(1,n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1 

            #NOTE: story:
            #it starts from 1st index, because we assume that the zero index is already sorted.
            #and then we initiate j as i. and then we go loop, in that loop if current element is smaller than it's previous element, we swap the values.
            # and decrease the value of j by 1 and check the values again and again.
arr = [5,3,3,6,2,8,1]
insertion_sort(arr)
print("The array after sorting: ")
print(*arr)
