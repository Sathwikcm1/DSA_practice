import math

def brute_force(n):
    cnt = 0
    #NOTE: this is simple algo, going through 1 to the number and counting the factors, if it is equal to 2 then it is a prime otherwise it's a decepticon.

    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        print(f"The number {n} is prime number.") 
    else:
        print(f"The number {n} is not a prime number.")

def optimal_approach(n):
    print("This is the optimal_approach:")

    cnt = 0
    #NOTE: so in this algo, instead checking till n, we can just check only till sqrt(n).
    #because the other half of that will be checked as well.
    # 
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt+=1
            #NOTE: the line below is to check if the counter part is not the same number.
            #example: n = 25 and i = 5, here, 5 * 5, so both of them is five, we only cnt it once so.
            if n//i != i:
                cnt+=1
    if cnt == 2:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

n = 23
brute_force(n)
optimal_approach(n)
