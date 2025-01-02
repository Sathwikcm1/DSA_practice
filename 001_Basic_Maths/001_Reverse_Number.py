#FIXME: Just return the reversed given number
# for example: x = 123 , return 321.

#TODO: reversing a number, we take the last digit out of the number by doing modulus we get the last digit.
# then we can add that to that rev_no variable which we initiated to zero at the beginning, if n < 0, we can still use the same function.
# but lil criminal by sending the negative of negative value to the function.
def reverse_Num(n):
    rev_no = 0
    if n < 0: #NOTE: handling the negative numbers part.
        return -reverse_Num(-x)
    while n:
        ld = n % 10 #NOTE: last digit of the number.
        rev_no = rev_no * 10 + ld #NOTE: reversing the number, 0*10+3, 3*10+2, 32*10+1 = 321.
        n = n//10 #NOTE: Integer division is important here. 
    return rev_no if rev_no <= 0x7fffffff else 0

n = 123
ans = reverse_Num(n)
print("The original number is : ",n)
print("The reversed number is : ",ans)
