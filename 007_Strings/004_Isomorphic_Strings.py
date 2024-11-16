#FIXME: Isomorphic Strings, let's s and t are two given strings.
# Two strings are said to be ismorphic if characters in s can be replaced to get t.
# example: egg, add: true
#   foo, bar: false.
#   paper, title: true.

def isIsomorphic(s,t):
    if s is None or t is None:
        return False 
    elif s == "" and t == "":
        return True 
    else:
        if len(s) != len(t):
            return False
        lookup = {}

        for i in range(0,len(s)):
            c1 = s[i]
            c2 = t[i]
            
            if c1 in lookup:
                if lookup[c1] != c2:
                    return False
            else:
                if c2 in lookup.values():
                    return False
                lookup[c1] = c2

    return True

s = "title"
t = "paper"

if isIsomorphic(s,t):
    print("It is isomorphic.")
else:
    print("it is not.")


