#HACK: find the nth fibonacci number and print the first N fibonacci numbers.
#FIXME: fibonacci sequence is a series of numbers where each number is the sum of preceding ones, usually starting with 0 and 1.(0,1,1,2,3,5,8..)

def nth_fibonacci(n):
    if n < 0:
        return "Input cannot be negative number for fibonacci sequence."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2,n+1):
            a,b= b,a+b
        return b

print(f"The fibonacci number for 7 is {nth_fibonacci(7)}")
