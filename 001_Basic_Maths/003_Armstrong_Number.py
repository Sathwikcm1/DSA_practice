#FIXME: Armstrong number is a number when the digits of the given number are raised to power of number of digits and add them
# the result will be the number itself
# example: 371 = 3^3 + 7^3 + 1^3

def basic_is_Armstrong(n):
    if n < 0:
        return False
    #NOTE: if the number is negative it is generally not considered for armstrong number.


    og_n = n #NOTE: copying the original number.
    num_digits = 0   #NOTE: This var will have the number of digits of the given number.
    temp_n = n  #NOTE: temporary value to loop over again and again.

    #HACK: counting the number of digits in the given number.
    if temp_n == 0:
        num_digits = 1
    else:
        while temp_n:
            temp_n//=10
            num_digits+=1

    #HACK: Actually adding the cube of each number to see if we get the same result or not.
    sum_of_powers = 0 #NOTE: this is the var that holds the result of the sum of powers.
    temp_n = og_n #NOTE: re-initialising the temp to the original number.

    while temp_n:
        last_digit = temp_n % 10
        sum_of_powers += last_digit ** num_digits
        temp_n //= 10

    return sum_of_powers == og_n


n = 371
if basic_is_Armstrong(n):
    print("The given number is Armstrong")
else:
    print("The given number is not Armstrong.")

#TODO: if we really want to make this easy you alwasy convert the number into a string.

def string_Armstrong(n):
    if n < 0:
        return False
    s = str(n)
    num_digits = len(s)

    sum_of_powers = 0

    for char_digits in s:
        digit = int(char_digits)
        sum_of_powers += digit ** num_digits

    return n == sum_of_powers
