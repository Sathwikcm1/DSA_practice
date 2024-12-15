#TODO: Merge sort is based on divide and Merge concept.
#TODO: it takes O(nlogn) time complexity.

def merge_sort(arr,low,high):
    if low>=high:
        return
    mid = (low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)


def merge(arr,low,mid,high):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left <= mid:
        temp.append(arr[left])
        left+=1
    while right <= high:
        temp.append(arr[right])
        right +=1

    #TODO: since the low values is updated, low is now pointing to mid element.
    # that's why if we subtract temp[i - low] that will give use the first element of the temp list which we can assign it to the original array.
    for i in range(low,high+1):
        arr[i] = temp[i-low]

arr = [3,2,4,5,2,6,8,1]
merge_sort(arr,0,len(arr)-1)
print(*arr)
#NOTE: adding that asterisk will open the list and print the elements of the list.

