#FIXME: To move all the zeroes in the array to the end of the array.
#example: arr = [1,0,2,0,3,3,0], output: arr = [1,2,3,3,0,0,0]

#TODO: the story of brute force, move all the non-zero elements to a temporary array. 
#Copy the numbers to original array and fill the rest with zeroes.
def brute_force(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    print(temp)
    temp_len = len(temp)
    print(temp_len)
    for i in range(temp_len):
        arr[i] = temp[i]
    print(arr)

    for i in range(temp_len,n):
        arr[i] = 0

    print(arr)

arr = [1,2,3,4,0,2,0,2,3,0]
print("The original array : ",arr)
brute_force(arr)
