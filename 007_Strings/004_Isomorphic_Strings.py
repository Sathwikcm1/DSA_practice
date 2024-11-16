#FIXME: Isomorphic Strings, let's s and t are two given strings.
# Two strings are said to be ismorphic if characters in s can be replaced to get t.
# example: egg, add: true
#   foo, bar: false.
#   paper, title: true.

#TODO: we use the concept of hasmap or lookup table.
def isIsomorphic(s,t):
    #NOTE: if the length of any of them is null, we return false.
    if s is None or t is None:
        return False 
    #NOTE: or if we find any of them contains the string as "" we return false.
    elif s == "" and t == "":
        return True 
    else:
    #NOTE: if the lenght of both the strings are not equal we return false.
        if len(s) != len(t):
            return False
        #NOTE: initialising the lookup table or dictionary.
        lookup = {}

        for i in range(0,len(s)):
            c1 = s[i] #NOTE: contains a character from the string s.
            c2 = t[i] #NOTE: contains a character from the string t.
            
            if c1 in lookup:
                #NOTE: if the c1 is present in the lookup check for it's value if it is not c2 then return False
                if lookup[c1] != c2:
                    return False
            else:
                #NOTE: if the c2 value is already present in the values, we return false.
                if c2 in lookup.values():
                    return False
                #NOTE: otherwise we add the key-value pair to the dictionary or lookup table.
                lookup[c1] = c2

    return True

s = "title"
t = "paper"

if isIsomorphic(s,t):
    print("It is isomorphic.")
else:
    print("it is not.")


