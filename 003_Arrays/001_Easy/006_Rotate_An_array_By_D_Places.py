#FIXME: The question is to rotate the given array to right by d no of places, for example, arr = [1,2,3,4,5], d = 3, output : arr = [4,5,1,2,3].

#TODO: The story of the brute force solution, we can just use a temporary array to put the elements till d, to the temporary array and then put the rest of the elements put back to the original array.
def brute_force(arr,k):
    n = len(arr)
    k = k%n  #NOTE: if the value of k > n, it will in range after this.
    if k == 0: #NOTE: even after that if the value of k is zero, that means they want the original array.
        return arr
    temp = [0] * n 
    #NOTE: copying the last k elements to the temp array.
    for i in range(k):
        temp[i] = arr[n-k+i]
    #NOTE: copying the remaining elements to the temp array.
    for i in range(n - k):
        temp[k+i] = arr[i]
    #NOTE: copying the whole temp array to the original array.
    for i in range(n):
        arr[i] = temp[i]
#TODO: The time complexity is O(2N), so basically O(N).


def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1 
        end -= 1

#TODO: The story of optimal, we can rotate the array till k, after we rotate from k + 1 to n, and then rotate the whole array.
def optimal(arr,k):
    n = len(arr)
    k = k%n #NOTE: again to make the k value valid, which less than n.

    if k == 0:
        return arr
    #NOTE: reverse the first half of the array. reverse(array, start, end) 
    reverse(arr,0,n-k-1)
    #NOTE: reverse the remaining half of the array.
    reverse(arr,n-k,n-1)
    #NOTE: Now reverse the whole array after reversing those halves.
    reverse(arr,0,n-1)
#TODO: The time complexity of the optimal approach is O(N).



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    k = 2
    print("Before rotating the array by k places: ", arr)
    brute_force(arr,k)
    print("After rotating the array by k places using brute_force approach: ",arr)


    arr = [1,2,3,4,5,6,7,8]
    print("The array before: ",arr)
    optimal(arr,k)
    print("The array after rotating the array by d places using optimal: ",arr)
