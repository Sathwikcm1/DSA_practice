#FIXME: Remove the repeated elements from a sorted array, all the elements in the array should be unique and different


from typing import List #NOTE: this is type hint, this is used to write it like a comment to let people know what you are using in the program. 

#TODO: Story of brute_force: we are putting all the elements into a set data structure which cannot contain duplicates, so it will get rid of the duplicates, now we can copy the elements from the set and put it to the original array.
def brute_force(arr: List[int]) -> int:
    #NOTE: we are basically return the lenght of the new array that contains only unique elements.
    st = set()
    for num in arr:
        st.add(num)
    len_st = len(st)
    j = 0
    for x in st:
        arr[j] = x 
        j += 1
    return len_st
#NOTE: This will take time complexity of O(n * log n + n)



#TODO: This is story of optimal solution: In this solution we use two pointers method.
#we have two pointers say i and j, we keep the i to the first element of the array and we start a loop from the j to len(arr).
#i will only be incremented if arr[i] != arr[j], again this is a sorted array.
def optimal(arr: List[int]) -> int:
    i = 0
    for j in range(1,len(arr),1):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1 #NOTE: since i will be incremented for the unique values found, i + 1 will be the length of the array.

if __name__ == "__main__":
    arr = [1,2,1,2,3,4,5,4]
    print("The original Array: ", arr) 
    # k1 = brute_force(arr)
    print("The after removing all the duplicates from the array: ")
    # for i in range(k1):
    #     print(arr[i], end = " ")
    # print()
    #
    print("The Two pointer method: Removing all the zeroes: ")
    k2 = optimal(arr)
    for i in range(k2):
        print(arr[i],end = " ")
    print()
