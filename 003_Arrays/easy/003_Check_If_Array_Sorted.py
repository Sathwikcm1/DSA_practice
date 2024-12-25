#FIXME: we have to check if the given array is sorted or not.
def brute_force(arr,n):
    #NOTE: This is obviously brute_force solution which takes O(N) time complexity.

    # we basically loop through the array starting from index 1, if arr[i] is less than the previous element arr[i-1] we return false otherwise true.
    for i in range(1,n):

        if arr[i] < arr[i-1]:
            return False 
    return True 


if __name__ == "__main__":
    arr = [2,5,6,7,8,10]
    n = len(arr)
    print("Brute force approach: ", "The array is sorted" if brute_force(arr,n) else "No, The array is not sorted.")
