
#FIXME: determine whether an integer is a palindrome.

#TODO: this is a simple algo, it's the same as reversing a number. 
# if the original number is equal to the reversed number then the number is a palindrome otherwise return False.
def isPalindrome(x):
    if x < 0:
        return False
    rev = 0
    if x >= 0 and x < 10:
        return True
    #NOTE: single-digit numbers (0-9) are palindrome since they are single-digit.
    copy = x
    while copy:
        last_digit = copy % 10
        rev = rev * 10 + last_digit
        copy = copy//10
    return x == rev #NOTE: this is the comparision that is really happening.

x = 121
if isPalindrome(x):
    print("This is Palindrome.")
else:
    print("This is not Palindrome.")


#NOTE: or you can just convert the number into a string and then it as easy as this.

def isPlanidrome_string_method(x):
    if x < 0:
        return False 
    s = str(x)
    return s == s[::-1]

print("This is using the string method, the given number: 10901")
if (isPlanidrome_string_method(10901)):
    print("The given number is a palindrome.")

