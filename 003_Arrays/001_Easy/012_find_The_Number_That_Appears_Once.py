#FIXME: In the given array, every element will be repeated twice except for one element we need to find that element and return it.

#TODO: So the brute force approach for this problem would be to,
#if one element is only reapeated once that means the total size of the array is even.


def brute_force(arr:[int])->int:
    n = len(arr)
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


if __name__ == "__main__":
    arr = [1,1,2,2,3,4,4]
    ans = brute_force(arr)
    print(ans)
