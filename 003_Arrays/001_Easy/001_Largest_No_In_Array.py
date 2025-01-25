#FIXME: To find the largest number in the array.

#TODO: Brute force is simple, sort the given array and return the last element of the sorted array.
def brute_force(arr):
    n = len(arr)
    arr.sort()
    return arr[-1]
#NOTE: The time complexity for the brute force approach is O(n * Logn), for sorting it first.

#TODO: The optimal approach, Instead of sorting the array, we will keep finding for the maximum element by going through the array.
def optimal(arr):
    n = len(arr)
    maxi = 0
    for i in range(n):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
#NOTE: Time complexity for this optimal approach is O(N).

if __name__ == "__main__":
    arr1 = [2 ,3 ,4, 5, 6, 10]
    print("The largest element in the given array is :", brute_force(arr1))
    print("The largest element in the given array using optimal approach: ", optimal(arr1))
    print(max(arr1)) #FIXME: the simplest possible way to return a maximum element of a list.
