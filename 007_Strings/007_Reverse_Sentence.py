#FIXME: In this question, we reverse the sentence where the words stays the same but the order of teh words is reversed.
#example: Input: s = "the sky is blue", Output: "blue is sky the"
#It should also erase all the trailing and leading extra space.

#TODO: so the plan is to split the sentence into words and return that list and then we convert that into a string and return it.
def reversed(s):
    s=s.split()
    #NOTE :previous line contains only list of words.
    s.reverse()
    ans=" ".join(s)
    ans.strip()
    return ans

s = "Hello Friend I Know but this is actually   happening   "
ans = reversed(s)
print(ans)

