#FIXME: The problem statement:
#Given a string containing parenthesis, determine if the string is valid or not.
#An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.


#TODO: Yes we use stack for this, 
#story: if we find the parenthesis in str, if it's a opening parenthesis we will put it in the stack.
#and then we pop the elements it should perfectly match opening parenthesis otherwise it will be considered False.
def isValid(s: str) -> bool:
    st = [] #NOTE: initializing the stack.
    for char in s: #NOTE: checking if the current char in the string is an opening parenthesis or not if it is , then we will add it to the stack.
        if char == '(' or char == '[' or char == '{':
            st.append(char)
        #NOTE: Otherwise we will check if the length of the stack is zero, if the current char is a closing parenthesis and then there is no opening parenthesis in the stack , then we should return false.
        else:
            if len(st) == 0:
                return False
            #NOTE: we will pop the last parenthesis to compare that with the current closing parenthesis, if they match we continue otherwise return false.
            lp = st.pop()
            if ( (char == ')' and lp == '(') or (char == '}' and lp == '{') or (char == ']' and lp == '[') ):
                continue 
            else:
                return False
    return len(st) == 0



if __name__ == "__main__":
    s = "()[{}()]"
    if isValid(s):
        print("True")
    else:
        print("False")
