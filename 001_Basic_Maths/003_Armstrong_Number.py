#FIXME: Armstrong number is a number when the digits of the given number are raised to power of number of digits and add them
# the result will be the number itself
# example: 371 = 3^3 + 7^3 + 1^3

def is_Armstrong(n):
    og = n 
    #NOTE: this is the original number copy. since the original will change after that while loop.
    sum = 0
    while n:
        #NOTE: Last digit is the mod of the original number.
        ld = n % 10
        #NOTE: sum is nothing but adding the cubes of each digit.
        sum += ld ** 3 
        n//=10

        #NOTE: if the sum is equal to the original number we return true.
    if og == sum:
        return True
    else:
        return False


n = 371
if is_Armstrong(n):
    print("The given number is Armstrong")
else:
    print("The given number is not Armstrong.")
