#FIXME: There will be two strings given, we have to add each character to the result string from each of the string.
#example; w1:"abc", w2:"pqr" and then res:"apbqcr"
#another example: w1:"a b c" and w1: " p q r" : res: "abpqrs"

def Merge_Strings(w1,w2):
    i = 0
    res=""
    while i < len(w1) or i < len(w2):
        if i < len(w1):
            res+=w1[i]
        if i < len(w2):
            res+=w2[i]
        i+=1
    return res


s1 = "abc"
s2 = "pqr"
print(f"String 1 is {s1} and String 2 is {s2}.")
res=Merge_Strings(s1,s2)
print("The Merged String is ",res)

