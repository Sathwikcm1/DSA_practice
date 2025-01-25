#FIXME: Example 1:                              page no : 01 and 02 in the new book.
#Input Format: N = 3, k = 5, array[] = {2,3,5} , where n is the size of the array and the k is the sum .
#Result: 2
#Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
#try example, arr=[5,2,3,1,9] , k = 10, n = 5.

from typing import List #this is used to type which type is being accepted as a parameter and which data type is to be returned. This is called type hinting. Type hinting is used to specify the types of the variables.

#TODO: This is the story of the brute_force approach:
#so we are basically finding the subarrays using the first two for loops and then we are adding the elements inside the for loops using the third for loop.
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
#NOTE: hashmap contains {sum,index}.
#TODO:
#first we will declare all the variables such as hashmap, sum, maxlen. sum is to calculate the sum of the subarray. and then we have the maxlen which is the result that we to return at the end.
#and then we have one for loop going through that we will be adding each element from the array to the sum variable, we will check if the sum is equal to the k, if it is we put that in maxlen, otherwise we will calculate the remaining by, sum-k and then we check if the rem is in there in the hashmap.
#if the rem is in hashmap we calculate the length. if the rem also is not present in the map and then we will add the sum and the index to the hashmap.

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




#FIXME: This only works if there are positive numbers in the array. This doesn't works if there are negative numbers too in the array.
#TODO: This is the optimal solution using two pointers:
#story: so the two pointers are left and right which initially pointing to the same 0th index.
# then we have maxlen and sum initialised with zeroth element, for the same purposes. 
def optimal(arr:[int],k:int)->int:
    n = len(arr)
    left, right = 0,0 #NOTE: these are the pointers.
    sum = arr[0] #NOTE: sum will be initiated to the first element in the array.
    maxlen = 0
    while right < n:
        while left <= right and sum >k: #NOTE: this is the not the first logic here, go to line 99 or 100th line.
            #NOTE: this is only applied when the sum value is greater than k, we need reduce the size of the subarray so we move the left pointer by one.
            sum -= arr[left]
            left+=1 

        #NOTE: this is just a normal check if it is equal to k or not.
        if sum == k:
            maxlen = max(maxlen, right-left+1)

        #NOTE: this is where the logic starts from the first. we increment the right pointer first and then we check if right is still less than or not , if it and then we add the current arr[right] element to sum.
        right+=1 
        if right < n:
            sum += arr[right]

    return maxlen #NOTE: at the end we return the maxlen.
#FIXME: time complexity: O(n).



if __name__ == "__main__":
    arr = [2,3,5,1,9]
    k = 10
    ans1 = brute_force(arr,k)
    ans2 = better_approach(arr,k)
    print(ans2)
    print(ans1)
    ans3 = better_two(arr,k)
    print(ans3)
    ans4 = optimal(arr,k)
    print(ans4)

