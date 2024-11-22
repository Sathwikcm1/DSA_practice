def brute_force(n,m):
    gcd = 1
    for i in range(1,min(m,n)+1):#TODO: because, it has to run till 5. not before that,the numbers are 5 and 10. so the min is 5.
        #NOTE: if both of them divided by i, the we can consider that to be gcd, for example : 1. but we need the greatest one . so we keep on looping.

        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

def better_approach(n,m):
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            return i
    return 1

def optimal_approach(n,m):
    while n > 0 and m > 0:
        if n > m:
            n %= m 
        else:
            m %= n
    return max(n,m)

n = 5
m = 10
print("Brute Force Approach: ", brute_force(n, m))
print("Better Approach: ", better_approach(n, m))
print("Optimal Approach: ", optimal_approach(n, m))
