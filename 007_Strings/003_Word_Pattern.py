#FIXME: :Given a pattern and a string str, find if str follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in
#pattern and a non-empty word in str.
# example : pattern = "abba", str = "dog cat cat dog" should return true. pattern =
#"abba", str = "dog cat cat fish" should return false. pattern = "aaaa", str = "dog cat
#cat dog" should return false. pattern = "abba", str = "dog dog dog dog" should
#return false


#TODO: basically using hashmap or lookup table in this question.
def wordPattern(pattern,str):
    #NOTE: if the pattern lenght or the str length is zero then return false.
    if pattern is None or str == None:
        return False
    else:
        len_str = len(str.split(" ")) #NOTE: calculating the length of the list of the words in the given string using split function.
        #NOTE: split function splits the string wherever " " is present return a list of words.
        len_pattern = len(pattern)
        #NOTE: comparing the values of lenght of pattern and the string list. if it same then it is ok otherwise return false.
        if len_str != len_pattern:
            return False 
        #NOTE: actually splitting the string now.
        str = str.split(" ")
        #NOTE: initialising the lookup table.
        lookup = {}
        #NOTE: the loop will run as long as the pattern itself.
        for i in range(0, len(pattern)):
            s = str[i]
            p = pattern[i]
            #NOTE: if p is already in lookup table, check for the value of this key it must contain "s" otherwise return false.
            if p in lookup:
                if lookup[p] != s:
                    return False
            else:
                if s in lookup.values():
                    return False
                #NOTE:if not already present in the lookuptable adding the key and value to the lookup table.
                lookup[p] = s 
        #NOTE: if the for loop completes then return true.
        return True 


pattern = "abba"
str = "dog cat cat dog"
if wordPattern(pattern,str):
    print("It is true.")
else:
    print("It is false.")

