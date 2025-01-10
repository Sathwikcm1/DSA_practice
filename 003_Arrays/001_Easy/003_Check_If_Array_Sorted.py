#FIXME: we have to check if the given array is sorted or not.
def brute_force(arr,n):
    #NOTE: This is obviously brute_force solution which takes O(N) time complexity.
    drop_count = 0
    # we basically loop through the array starting from index 1, if arr[i] is less than the previous element arr[i-1] we return false otherwise true.
    for i in range(n):
        
        if arr[i] > arr[(i+1) % n]:
            drop_count += 1 
            if drop_count > 1:
                return False 
    return True 


if __name__ == "__main__":
    arr = [2,5,6,7,8,10]
    arr2 = [3,4,5,1,2] #this array should also be considered sorted since it is only rotated to left by 2 places.
    n = len(arr2)
    print("Brute force approach: ", "The array is sorted" if brute_force(arr,n) else "No, The array is not sorted.")
