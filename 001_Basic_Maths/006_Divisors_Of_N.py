import math
#FIXME: Return the divisors for the given number

def brute_force(n):
    print("\n Brute Force Approach: ")
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end = " ")

#TODO: the brute force is simple enough and takes O(n). 
#you go every number from 1 to n and check if it divides the number n or not if it does we print it out.


def optimal(n):
    print("\n Optimal Approach: ")
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i, end=" ")
            if i != n//i: 
                print(n//i, end= " ")

n = 10
optimal(n)
brute_force(n)
