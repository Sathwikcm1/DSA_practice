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
            #NOTE: if the number is 25, then 25//i: let's say i is 5, it will give us 5, so that is equal to i. 
            #? Example: n = 36, i = 4.

            # n % i == 0 → 36 % 4 == 0 ✅

            # n // i = 36 // 4 = 9

            # Since 9 != 4, the condition is true, so you add another count for the divisor 9.
            # This way, both 4 and 9 are counted.
    if cnt == 2:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

n = 23
brute_force(n)
optimal_approach(n)
