#FIXME: This is a linear search in an array.

#TODO: just linear search , search through the whole array from starting to end of the array.
def search(arr: [int], n :int, k:int) -> bool:
    for i in range(n):
        if arr[i] == k:
            return i 
    return -1


if __name__ == "__main__":
    arr= [1,2,4,5,6,7,8]
    k = 4
    n = len(arr)
    print(search(arr,n,k))
