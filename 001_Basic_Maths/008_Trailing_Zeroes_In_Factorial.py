#FIXME: find the number of trailing zeroes in N!
#HACK: in the last page of the new book it has been explained with the example of 15 check it out.
#for example: in 5!(120) = 1, in 10!(3,628,800) = 2.

def trailing_zeroes_in_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    count = 0
    i = 5
    #NOTE: for example let's take 15, number of 5 multiples is 3 right.
    while n//i >=1 : #NOTE: this loop will run till the 15/3 is greater or equal to 1.
        count += n//i #NOTE: for the first loop this directly updated to 3.(since n//i is 3)
        i *= 5 #NOTE: this is to check the next power of 5(5^2) how many times that is being repeated till we reach the number n.
    return count

print(f"number of trailing zeroes for the factorial of {trailing_zeroes_in_factorial(10)}")

