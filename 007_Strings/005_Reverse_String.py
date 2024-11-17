#FIXME: given hello we have to return olleh.

def reverse(s):
    #NOTE: since in python strings are immutable. we convert them into mutable data type like list by writing below code.
    
    #NOTE: this will return a list of characters of the string "s".
    current_str = [char for char in s]
    i = 0
    j = len(s) - 1
    #TODO: story: the loop will go till half of the string swapping characters from both sides.
    while i < j:
        temp = current_str[i]
        current_str[i] = current_str[j]
        current_str[j] = temp
        j -= 1
        i += 1

    #NOTE: this is the opposite of converting string into list. this is converting list into string.

    return "".join(current_str)


s = "sathwik"
ans = reverse(s)
print("Reversed string: ",ans)
