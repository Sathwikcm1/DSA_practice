#FIXME: Count Maximum repeating ones consecutively.
#example: prices = {1, 1, 0, 1, 1, 1}, output : 3, because there are three ones consecutively.


def solution(arr):
    max_count, count = 0,0

    for i in range(len(arr)):
        if arr[i] == 1:
            count+=1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

arr = [1,2,1,1,1,0,1,1]
ans=solution(arr)
print("The number of maximum consecutive ones are ",ans)

