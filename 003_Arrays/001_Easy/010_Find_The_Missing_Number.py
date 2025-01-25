#FIXME: Find the missing number in an array of numbers 1 to n-1.
#the array is not sorted in the beginning.


def brute(arr,n):
    #NOTE: The brute force approach is to sort the array which will take O(n logn) time complexity 
    #And then we have to check if the index has the same number otherwise we return the index.
    arr.sort()
    for i in range(1,n): #NOTE: it starts from 1, because that's where numbering is starting, 1,2,3..., not 0,1,2,3...
        if i!=arr[i-1]:
            return i
    return -1
#NOTE: The total time complexity is O(N log N)




#TODO: Still not the optimal one, we can just use hash_array instead of sorting the array itself we can use hashmap to record the count of the each number in given array.
#FIXME: this is hash array not hashmap, that is why we are not using any .get method or anything.
def Using_Hash(arr,n):
    hash_array=[0]*(n+1) #NOTE: this is initializing array with zeroes with the size of the given array.

    #NOTE: firstly you are not vegeta! jk, we increment the given elements in the hash_array.
    for i in range(n-1):
        hash_array[arr[i]] += 1 

    #NOTE: In here again, we go through the hash_array to find which one has zero has it's value. and we return that index.
    for i in range(1, n+1): #NOTE: again , the index starts from 1, because the numbering starts from inside the zero , numbering means elements in the array starts from 1.
        if hash_array[i] == 0:
            return i 
    return -1


#TODO: story of optimal:
# we will use the sum of all the elements in the array, which will be compared to actual_sum of the numbers from 1 to n-1.
def Optimal(arr,n):
#NOTE: Using the power of friendship, Nah using meth.
    total_sum = (n * (n+1)) // 2
    #NOTE: Calculated the actual sum of 1 to N numbers.
    actual_sum = 0
    for i in range(n-1):
       actual_sum+=arr[i]
    ans=total_sum - actual_sum
    return ans

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,8,9]
    n = len(arr)
    ans1 = brute(arr,n)
    ans2 = Using_Hash(arr,n)
    ans3 = Optimal(arr,n)
    if ans1 != -1:
        print("The missing number in the array is: ", ans1, ".")
    else:
        print("There was no missing number in the given array.")

    if ans2 != -1:
        print("The missing number in the array is: ", ans2, ".")
    else:
        print("There was no missing number in the given array.")
    if ans3 != -1:
        print("The missing number in the array is: ", ans3, ".")
    else:
        print("There was no missing number in the given array.")
