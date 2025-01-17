#FIXME: Example 1:
#Input Format: N = 3, k = 5, array[] = {2,3,5}
#Result: 2
#Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.


from typing import List

#TODO: This is the story of the brute_force approach:
# we have 3 loops here, first outer loop is the starting index of the sub array and the next inner loop is the ending index of the sub array.
# and the inner most loop is for calculating the sum of that partiuclar sub array, after caclulating we check if it is equal to target or not.
# 
def brute_force(arr: [int], k:int) -> int:
    n = len(arr)
    length = 0

    for i in range(n): #NOTE: this is the starting index of the subarray.
        for j in range(i,n): #NOTE: this is the ending index of the subarray.
            s = 0               #NOTE: this is to calculate the sum of the subarray.
            for K in range(i,j+1):
                s += arr[K]
            if s == k: #NOTE: we check if it equal to sum, if it is we return the current lenght of the subarray, which is given  by j - 1 + 1, 
                length = max(length, j - i + 1)
    return length 
#FIXME: Time complexity of this algo is O(N^3).




#TODO: This is the better apporach :
#do we really need the third loop just to caluclate the sum of the sub array, we can do it while creating the inner for loop itself. by adding the current element to the sum 

def better_approach(arr:[int],k:int)->int:
    n = len(arr)
    length = 0
    for i in range(n):
        s = 0
        for j in range(i,n):
            s+=arr[j]
            if s == k:
                length = max(length,j-i+1)

    return length

#FIXME: This will still take O(N^2) for time complexity.




#TODO: Next better approach is to hashmap.

def better_two(arr:[int],k:int)->int:
    n = len(arr)
    SumMap= {} #NOTE: hashmap  being used to store the sum and the current index.
    sum = 0    #NOTE: sum is calculate the sum as we go through the loop.
    maxLen = 0 #NOTE: maxLen will have the answer for this question.

    for i in range(n):  #NOTE: we go through the loop with this one.
        sum += arr[i]   #NOTE: we add the current element with the sum.
        if sum == k:    #NOTE: if added sum is the value of the k, then we should return the index + 1 value.
            maxLen = max(maxLen, i+1)

        rem = sum - k  #NOTE: if not, we will calculate the remaining , i.e. k - sum, 

        #NOTE: we will check if the remaining part is present in the hashmap or not if it is then we 
        #have to return the index, we calculate the length by i - SumMap[rem]
        if rem in SumMap:
            length = i - SumMap[rem]
            maxLen = max(maxLen, length)
        if sum not in SumMap:
            SumMap[sum] = i

    return maxLen




#TODO: This is the optimal solution using two pointers:
def optimal(arr:[int],k:int)->int:
    n = len(arr)
    left, right = 0,0 #NOTE: these are the pointers.
    sum = a[0] #NOTE: sum will be initiated to the first element in the array.
    maxLen = 0
    while right < n:
        while left <= right and sum >k:
            


if __name__ == "__main__":
    arr = [2,3,5,1,9]
    k = 10
    ans1 = brute_force(arr,k)
    ans2 = better_approach(arr,k)
    print(ans2)
    print(ans1)
    ans3 = better_two(arr,k)
    print(ans3)

