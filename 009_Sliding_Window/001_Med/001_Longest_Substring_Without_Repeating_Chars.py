#FIXME: Given a String, find the length of the longest substring without any repeating character.
# This is in page no : 4

#TODO: Brute force approach: 
#we will be using a hash_map obviously. so it will take around O(n^2) time complexity  for this.
#we will check if the current character is present in the hash_map or not , if it is present then we will calculate 
#the max_len and then break out of the loop. and if not we will make the hash_map value as 1.
def brute(s:str)->int:
    if not s:  #NOTE: if the length of the given string itself is zero then we will simple return zero. 
        return 0
    if len(s) == 1: #NOTE: if the lenght of the given string is one, then we return one. cuz if the length itself is one, tf you looking for? 
        return 1
    max_len = 0 #NOTE: initializing the maxlen variable.
    for i in range(len(s)):
        hm = {} #NOTE: initializing the hash_map.
        curr_len = 0
        for j in range(i,len(s)):
            if s[j] in hm:
                break
            else:
                hm[s[j]] = 1
                curr_len += 1 #NOTE: the current length is increased as the character is pushed into the hashmap.
        max_len = max(max_len,curr_len) #NOTE: if the character is present in the maxlen is calculated and stored.
    return max_len

#HACK: Time complexity: (N^2) and space complexity: O(256), cuz that is the size of the hash_map.




#TODO: The better solution: Two pointer method.
#the left pointer is used to track the starting point of the substring and the right pointer is used to end of the substring.
def optimal(s:str)->int:
    hm = {} #NOTE: initializing hash_map.
    l = 0 #NOTE: left pointer.
    maxLen = 0 #NOTE: answer holder.

    for r in range(len(s)): #NOTE: r is the right pointer here.
        if s[r] in hm and hm[s[r]] >= l: #NOTE: l is only updated if the s[r] is present in the current substring(second if condition).
            l = hm[s[r]] + 1
            
        curr_len = r - l + 1
        maxLen = max(maxLen,curr_len)

        hm[s[r]] = r
    return maxLen


s = 'abcabcbb'
print('The lenght of the substring is : ',optimal(s))




#HACK: Notes:
#the sliding window is a special application of two pointer approach.
