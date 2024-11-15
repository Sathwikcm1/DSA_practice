#FIXME: this is the question: 
#FIXME: there are two strings given s and t.write a function to determine if t is an anagram of s.
#FIXME: ex: s = "rat" and t = "car", return false. s = "anagram" , t = "nagaram", return true.https://leetcode.com/problems/valid-anagram/

def isAnagram(s,t):
    #TODO: simple method we just have to check if the two strings are of the same length at first.
    #TODO: if not we return false. if not we go the check sorted strings both of them are same or not. simple.
    if len(s) != len(t):
        return False 
    elif sorted(s) == sorted(t):
        return True 
    else:
        return True

s = "hii"
t = "ihii"
if isAnagram(s,t):
    print("They are anagrams.")
else:
    print("They are not anagrams.")

#NOTE: if one is string is an anagram of another if it contains all the characters from the other string.
