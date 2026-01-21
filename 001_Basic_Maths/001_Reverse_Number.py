# FIXME: Just return the reversed given number
# for example: x = 123 , return 321.

# TODO: reversing a number, we take the last digit out of the number by doing modulus we get the last digit.
# then we can add that to that rev_no variable which we initiated to zero at the beginning, if n < 0, we can still use the same function.
def reverse_Num(n):
    rev_no = 0
    if n < 0:  # NOTE: handling the negative numbers part.
        # TODO: handling this is easy, you send the negative of the result of the function.
        return -reverse_Num(-n)
        # NOTE: and we are feeding the same negative number to the function and then returning the negative of that result.
    while n:
        ld = n % 10  # NOTE: last digit of the number.
        # NOTE: reversing the number, 0*10+3, 3*10+2, 32*10+1 = 321.
        rev_no = rev_no * 10 + ld
        n = n//10  # NOTE: Integer division is important here.
    return rev_no if rev_no <= 0x7fffffff else 0


n = -10
ans = reverse_Num(n)
print("The original number is : ", n)
print("The reversed number is : ", ans)


# NOTE: In python there is no default integer size like it is there in c or c++ or java for int 32 bits and for long 64 bits, python handles it differently, arbitrary precision. the size allocated is arbitrary and grow as required.
# so we don't need to write that 10th line in the actual code.
#

# TODO: Leetcode:

Class Solution():
    def reverse(self, n):
        rev_no = 0
        if n < 0:
            return -self.reverse(-n)
        elif n == 0:
            return 0
        while n:
            ld = n % 10
            rev_no = rev_no * 10 + ld
            n //= 10
        if rev_no < -2**31 or rev_no > 2**31 - 1:
            return 0
        return rev_no
