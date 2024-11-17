
#FIXME: determine whether an integer is a palindrome.

#TODO: this is a simple algo, it's the same as reversing a number. 
# if the original number is equal to the reversed number then the number is a palindrome otherwise return False.
def isPalindrome(x):
    if x < 0:
        return False
    rev = 0
    copy = x
    while copy:
        rev = rev*10 + copy % 10
        copy = copy//10
    return x == rev or x == rev//10

x = 121
if isPalindrome(x):
    print("This is Palindrome.")
else:
    print("This is not Palindrome.")
