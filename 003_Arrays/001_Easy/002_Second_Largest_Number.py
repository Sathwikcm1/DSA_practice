#FIXME: Find the second largest number present in the given array.

#TODO: Story of brute_force: 
#so we first initiate two variables named largest and second_largest. which will hold the respective values.
#so then we find the largest number using a for loop using max function.
#After that We sort the array and then we come from the last checking if the element is not largest then the element we find will be the second largest element.
def brute_force(arr):
    largest = float('-inf') #NOTE: this initializes the largest variable to negative infinity. This cannot be done using int or any other data type.
    s_largest = float('-inf')
    s_smallest = float('inf')
    
    for num in arr:
        largest = max(num,largest)
    #NOTE: so at this point we have both the smallest and the largest element in the array , now we want to find the second smallest and second largest elements of the array.
    arr.sort()

    for i in range(len(arr) - 2, -1 , -1):
        if arr[i] != largest:
            s_largest = arr[i]
            break
    return s_largest
#NOTE: Time complexity of the brute force is O(n * logn)

def s_smallest_element(arr):
    smallest = float('inf')
    s_smallest = float('inf')
    for num in arr:
        if num < smallest:
            smallest = num
    arr.sort()
    for i in range(1,len(arr)-1,1):
        if arr[i] != smallest:
            s_smallest = arr[i]
        break
    return s_smallest


#TODO: Story of better: So we first again will initiate two varaibles largest and s_largest , initiated to infinity..
#And then we start to find the largest using the same method(for loop). So finding the second_largest, is simple, coming from the end of the array, if the element is grater than the s_largest and not equal to largest element make it as s_largest element.
def better(arr):
    largest = float('-inf')
    s_largest = float('-inf')

    for num in arr:
        largest = max(num,largest)

    for num in arr:
        if num > s_largest and num != largest:
            s_largest = num
    return s_largest

def s_smallest_better(arr):
    smallest = float('inf')
    s_smallest = float('inf')

    for num in arr:
        smallest = min(smallest,num)
    
    for i in range(len(arr)-1):
        if arr[i] < s_smallest and arr[i] != smallest:
            s_smallest = arr[i]
    return s_smallest
#NOTE: Time complexity of better approach is O(N).


#TODO: The story of the optimal approach , this will take O(N), the better one takes O(2N).
#again, same large and s_largest are initiated to infinity and then we have only one for loop.
# we go ahead with that , if arr[i] is greater than the largest variable, make the s_largest and the current largest element and then make the largest as the new arr[i]. so in that we keep track of both largest and the second largest elements in the array.
def optimal(arr):
    largest = float('-inf')
    s_largest = float('-inf')

    for i in range(len(arr)):
        if arr[i] > largest:
            s_largest = largest
            largest = arr[i]
        elif arr[i] > s_largest and arr[i] != largest:
            s_largest = arr[i]
    return s_largest


if __name__ == "__main__":
    print("This the original array: ")
    arr = [3,4,2,6,7,8,1]
    print(arr)
    print("The largest element using optimal solution: ", optimal(arr))
    print("The largest element using brute foruce solution: ", brute_force(arr))
    print("The largest element using better : ", better(arr))

