#FIXME: Given a string, determine if it is a palindrome or not considering only alphanumeric characters and ignoring cases.
#FIXME: ex: A man, a plan, a canal: Panama" is a palindrome. "race a car" is
#FIXME: not a palindrome.
import re
#TODO: we need to import re for this one.

#TODO: Palindrome: Reads the same when the string is reversed.
def isPalindrome(s):
#NOTE: for this we have to figure just to get the characters out of the given strings.
#NOTE: ignoring all the other characters like special ones and etc.
# if the length of the strings is zero it is still considered as a palindrome.
    if len(s) == 0:
        return True
    else:
        s = s.lower()
        # convert everything into lowercase
        start = 0
        #NOTE: the new string only contains alpha numeric values nothing else.
        # here we do that using regex, we can also use a simple for loop for that.
        new_string = re.sub(r"[^a-zA-Z0-9]","",s)
        end = len(new_string)-1
        while start < end:
            if new_string[start] == new_string[end]:
                start = start+1
                end = end - 1
            else:
                return False
        return True

def ispalindrome2(s):
    #TODO: how we could do the same using a for loop instead of regex.
    for char in s:
        new_string = ""
        if char.isalnum():
            new_string += char.lower()

    start,end = 0,len(new_string)-1
    while start < end:
        if new_string[start] == new_string[end]:
            start = start+1
            end = end - 1
        else:
            return False
    return True


s = "A man, a plan, a canal: Panama"
if ispalindrome2(s):
    print("The given string is a plalindrome.")
else:
    print("The given string is not a Palindrome.")


if isPalindrome(s):
    print("The given string is a plalindrome.")
else:
    print("The given string is not a Palindrome.")
