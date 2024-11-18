#FIXME:: basically have to return true of false, by checking if the given strings matches the parenthesis or not.
# example: he brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]"
#and "([)]" are not.

def matches(open,close):
    openings = "([{"
    closings = ")]}"
    return openings.index(open) == closings.index(close)


#TODO: this is where we start.
def isValid(s):
    #NOTE: if the string is empty we return false.
    if s == "":
        return False 
    
    stack = []
    balanced = True 
    index = 0
    #NOTE: initialising a stack, a boolean value and an index to travel through the string.
    while index < len(s) and balanced:
        #NOTE:while the index is less than the length of the given string and balanced is true. 
        symbol = s[index]
        #NOTE: if the symbol is present in the opening, we push it to the stack.
        if symbol in "([{":
            stack.append(symbol)
        else:
            #NOTE: if the symbol is a closing one, and if the  stack is empty that means the parenthesis is unmatched. we return false.

            if stack == []:
                balanced = False 
            #NOTE: take the top element and call the function mathches(top,symbol) which checks the matching parenthesis or not.
            else:
                top = stack.pop()
                if not matches(top,symbol):
                    balanced = False 
                    #NOTE: if its not matching then we need to make balanced as False.
        index = index + 1

    if balanced and stack == []:
        return True
    else:
        return False

s = "([{}])"
if isValid(s):
    print("The string is valid.")
else:
    print("The strings is not valid.")
