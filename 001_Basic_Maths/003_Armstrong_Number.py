#FIXME: Armstrong number is a number when cube the digits of the given number and add them
# the result will be the number itself
# example: 371 = 3^3 + 7^3 + 1^3

def is_Armstrong(n):
    og = n 
    sum = 0
    while n:
        ld = n % 10
        sum += ld ** 3 
        n//=10

    if og == sum:
        return True
    else:
        return False


n = 371
if is_Armstrong(n):
    print("The given number is Armstrong")
else:
    print("The given number is not Armstrong.")
