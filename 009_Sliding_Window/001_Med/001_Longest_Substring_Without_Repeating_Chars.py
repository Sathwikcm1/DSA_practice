#FIXME: Given a String, find the length of the longest substring without any repeating character.
# This is in page no : 4

#TODO: Brute force approach: 
#we will be using a hash_map obviously. so it will take around O(n^2) time complexity  for this.
#we will check if the current character is present in the hash_map or not , if it is present then we will calculate 
#the max_len and then break out of the loop. and if not we will make the hash_map value as 1.
def brute(s:str)->int:
    if not s: 
        return 0
    if len(s) == 1:
        return 1
    max_len = 0
    for i in range(len(s)):
        hm = {}
        curr_len = 0
        for j in range(i,len(s)):
            if s[j] in hm:
                break
            else:
                hm[s[j]] = 1
                curr_len += 1
        max_len = max(max_len,curr_len)
    return max_len

#HACK: Time complexity: )(N^2) and space complexity: O(256), cuz that is the size of the hash_map.

s = 'abcabcbb'
print('The lenght of the substring is : ',brute(s))
