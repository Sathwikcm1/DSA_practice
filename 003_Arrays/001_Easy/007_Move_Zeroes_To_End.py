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
def optimal(arr):
    n=len(arr)

arr = [1,2,3,4,0,2,0,2,3,0]
print("The original array : ",arr)
brute_force(arr)
