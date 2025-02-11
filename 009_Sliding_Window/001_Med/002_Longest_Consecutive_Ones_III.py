#FIXME: The problem statement : Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.




#TODO: Brute Force Approach: 
#so we can change the problem name to this also, to simplify the question : longest subarray with at most k no of zeroes
#generate all the sub arrays first using two for loops.so we will go on checking every single subarray if it has two zeroes at most and the length of each sub array and the maximum length of one of the sub array is recorded in maxLen variable and then we return the maxLen.


def brute(nums:[int],k)->int:
    n = len(nums)
    maxLen = 0 #NOTE: The variable holds the answer i. e. Maximum Length of the sub array.

    for i in range(n):
        no_of_zeroes = 0
        for j in range(i,n):
            if nums[j] == 0: #NOTE: if the current element is zero , increment the no_of_zeroes variable.
                no_of_zeroes += 1
            if no_of_zeroes <= k:
                cur_len = j - i + 1
                maxLen = max(cur_len,maxLen)
            else:
                break #NOTE: if the number of zeroes, less than or equal to 2.
    return maxLen

#HACK: Time complexity of brute force : O(n^2).


#TODO: This is the optimal code, using sliding window Approach.
def optimal(nums:[int],k:int) -> int:
    n = len(nums)
    maxLen = 0 #NOTE: stores the answer.
    left = 0 #NOTE: this is the left pointer , starting of the subarray or the window.
    zero_count= 0 #NOTE: stores the no of zeroes in the current subarray.

    for right in range(n):
        if nums[right] == 0: #NOTE: if the number that is pointed by right pointer is zero, we increment the no_of_zeroes counter.
            zero_count += 1

        #NOTE: if zero count is greater than what it is suppose to be , we give a loop which basically shrinkens the window by incrementing the left pointer.
        while zero_count > k:
            if nums[left] == 0: #NOTE: if the left pointing number is zero we will increment left and then windows will become smaller.
                zero_count -= 1 #NOTE: obv this also changed accordingly.
            left += 1
        maxLen = max(maxLen,right-left + 1)
    return maxLen


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
n = brute(nums,k)
s = optimal(nums,k)
print("The length is : ", n)
print("The optimal value length is: ", s)
