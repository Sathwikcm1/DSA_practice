def brute_force(n,m):
    gcd = 1
    for i in range(1,min(m,n)+1):#TODO: because, it has to run till 5. not before that,the numbers are 5 and 10. so the min is 5.
        #NOTE: if both of them divided by i, the we can consider that to be gcd, for example : 1. but we need the greatest one . so we keep on looping.

        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd

#TODO: this is better_approach due to it comes from the backward instead of going from 1 to n, it comes from n to 1.
#so the chances are finding it faster here.
def better_approach(n,m):
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            return i
    return 1

#TODO: it is based on the euclidean algorithm: gcd of two numbers won't change if the larger number is replaced by it's remainder when it is divided by
# by the smaller number. Repeat this process until one of the number becomes zero.
def optimal_approach(n,m):
    while n > 0 and m > 0:
        if n > m:
            n %= m
        else:
            m %= n
    return max(n,m)

def brute_force_lcm(n,m):
    gcd = brute_force(n,m)
    lcm = abs(n * m) // gcd
    return lcm
#TODO: the same thing we can do for better_approach adn optimal_approach.


n = 5
m = 10
print("Brute Force Approach: ", brute_force(n, m))
print("Better Approach: ", better_approach(n, m))
print("Optimal Approach: ", optimal_approach(n, m))
print("LCM using the formula: lcm(a,b)=(a*B)//(GCD(a,b))")
print(brute_force_lcm(n,m))
