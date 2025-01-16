#FIXME: In the given array, every element will be repeated twice except for one element we need to find that element and return it.

#TODO: So the brute force approach for this problem would be to,
#if one element is only reapeated once that means the total size of the array is even.
#story: we got two for loops, one loop will have the element[arr[i]], we will take it as num, and then we have another for loop, the inner one is only required for comparing this num, to increment the count.
#if we find the num equivalent to any other number we increment, after the inner for loop , we check if the count is equal to one, that means the num is only present one time and we return that element.


def brute_force(arr:[int])->int:
    n = len(arr)
    #NOTE: checking the lenght is equal to even or not. because if one element is only once repeated the lenght of the array cannot be even.
    if n % 2 == 0:
        return -1
    for i in range(n):
        cnt = 0
        num = arr[i]
        for j in range(n):
            if arr[j] == num:
                cnt+=1
        if cnt == 1:
            return num
    return -1
#NOTE: this will take the time complexity as O(N^2)



#TODO: The better solution, we use the hashmap or hasharray for this one.
def better_solution(arr):
    n = len(arr)
    maxi = max(arr) #NOTE: yes, this will the give the max element present in the array.
    #NOTE: The reason we calculated this, to initiate the hash array till the max element so that we can increment till there, since we are using hasharray we have to do it.
    ha = [0] * (maxi + 1)  #NOTE: initialising the hasharray with zeroes.

    #NOTE: incrementing the count for each element. (O(N))
    for i in range(n):
        ha[arr[i]] += 1

    for i in range(len(ha)): #NOTE: checking if the count of the num is 1 or not. O(n), not the full lenght, until we find the single repeated element, it is dynamic.
        if ha[arr[i]] == 1:
            return arr[i]
    return -1 #NOTE: if no number is repeated once, then we return -1.

#TODO: This again will take O(2N) time complexity.
#FIXME: the above hasharray code will work if the given array has only postive numbers, if it contains negative numbers it will throw index out of bound for list error.
#TODO: For that we gonna have to use hash_map instead of hasharray. told ya mf.

def better_solution_using_hashmap(arr):
    n = len(arr)
    count = {} #NOTE: this is the dictionary init.
    for num in arr:
        if num in count: #NOTE: first we check if it is already present in the dictionary or not, if it is we just increment the value of the key.
            count[num] += 1
            #NOTE: if the key is not present in the dictionary we will assign 1 to the value.
        else:
            count[num] = 1

    #NOTE: we check if the value of the key is one or not , if it is we return the key, which is num.
    for num in count:
        if count[num] == 1:
            return num

    return -1




#TODO: This is the optimal solution for the question.
# Using xor , if the the same values are xored with each other , they will cancel out, 
# so for our question, if the array has same elements are repeated twice and we xorr them nothing will remain except for the element that is only repeated once.
def optimal(arr):
    xorr = 0
    for num in arr:
        xorr ^= num 
    return xorr
#NOTE: if the array length is even the xorr will return 0, in which case we have to check that.

if __name__ == "__main__":
    arr = [1,1,2,2,3,4,4]
    ans = brute_force(arr)
    ans2 = better_solution(arr)
    print(ans2)
    print(ans)
    ans3 = optimal(arr)
    print(ans3)
