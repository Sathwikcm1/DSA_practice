#FIXME: To move all the zeroes in the array to the end of the array.
#example: arr = [1,0,2,0,3,3,0], output: arr = [1,2,3,3,0,0,0]

#TODO: the story of brute force, move all the non-zero elements to a temporary array. 
#Copy the numbers to original array and fill the rest with zeroes.
def brute_force(arr):
    n = len(arr)
    temp = [] #NOTE: This is the temp array.
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])#NOTE: putting all non-zero elements to the temporary array first.
    temp_len = len(temp) #NOTE: Calculating the length of the temp array.
    for i in range(temp_len): #NOTE: copying all the elements from temp to original array.
        arr[i] = temp[i]
    #NOTE: Filling the remaining space in array with them zeroes.
    for i in range(temp_len,n):
        arr[i] = 0
#TODO: Time complexity for this brute force approach:  O(2N)


#TODO: Story of optimal: Two pointer method, alwasy try to shift rather putting it to another container.
#So two pointers will be there i and j.
def optimal(arr: [int]) -> [int]:
    n=len(arr)
    #NOTE: we will check for the first zero in the array, by using one for loop.
    j = -1 #NOTE: initialising j to -1.
    for i in range(n): 
        if arr[i] == 0:
            j = i
            break
    #NOTE: even after finding the first zero element in the array, j is still showing -1 then it means there is no zero present in the current array.
    if j == -1:
        return arr
    #NOTE: now we compare the rest of the array to the current zero elements. if the next element is not zero we will swap it the next element and increment j.
    for i in range(j+1,n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

arr = [1,2,3,4,0,2,0,2,3,0]
print("The original array : ",arr)
brute_force(arr)
optimal(arr)
print("After moving all the zeroes to the end of the array ,The array elements are : ",arr)
