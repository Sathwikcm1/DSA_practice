#FIXME: given a string and an integer k, we gotta find the max length of a substring, where you can select k number of characters in a substring and change it to any upper character.
#example: Example 2:
#
#Input: s = "AABABBA", k = 1
#Output: 4
#Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#The substring "BBBB" has the longest repeating letters, which is 4.
#There may exists other ways to achieve this answer too.


#TODO: This is the brute force, we will generate all the substrings with this one, and then we use a hashmap to keep track of freq of each character in the substring and then find the changes required for the current substring and calculate the maxLen if the changes is less than or equal to k and then return the calculated maxLen value.
def brute(s:str,k:int)->int:
    n = len(s)
    maxLen = 0
    for i in range(n):
        char_counts = {} #NOTE: dictionary to maintain the freq of each character in the current substring.
        maxFreq = 0 #NOTE: the max freq of any character in the current substring.
        
        for j in range(i,n):
            char_counts[s[j]] = char_counts.get(s[j],0) + 1 #NOTE: incrementing the values of chars.
            maxFreq = max(maxFreq,char_counts[s[j]]) #NOTE: calculate the maxFreq of the substring.


            changes = (j-i+1) - maxFreq #NOTE: by doing this, we will be calculating the number of characters that we will be replacing with the maxFreq character. in here we won't actually be doing it because we just have to return the int not the whole substring.


            if changes <= k: #TODO: if the changes are less than or equal to k value then we update the maxLen value otherwise we break out of the loop.
                maxLen = max(maxLen,j-i+1)
            else:
                break
    return maxLen
#HACK: Time complexity is O(n^2) and space complexity is O(n).




#TODO: This is the optimal version of it, This uses sliding window 
def optimal(s:str,k:int)->int:
    n = len(s)
    l = 0 #NOTE: right and left pointers.
    r = 0
    maxLen = 0
    maxFreq = 0
    char_counts = {} #NOTE: dictionary to count the frequency of the characters.

    for r in range(n):
        char_counts[s[r]]=char_counts.get(s[r],0) + 1 #NOTE: update the map.
        maxFreq = max(maxFreq,char_counts[s[r]]) #NOTE: calculate the maxFreq of the current window.

        #TODO: if the validity check fails(len-maxFeq <= k) , then we have to shrink the window itself.
        while (r - l + 1) - maxFreq > k:
            #NOTE: if it happens, we decrement the first character frequency in the map of the current window.
            char_counts[s[l]] -= 1
            l += 1 #TODO: we increment the left pointer so that window becomes smaller
            #TODO: after that we check for maxFreq again and calculate it since the map has been tampered.


            maxFreq = 0
            for count in char_counts.values():
                maxFreq = max(maxFreq,count)
                #NOTE: calculated the maxFreq.

        maxLen = max(maxLen,r-l+1) #NOTE: After all that shit, now we calculate the maxLen for each window.
    return maxLen



def main():
    test_cases = [
        ("AABABBA",1),
        ("ABAB",2),
        ("AAAA",0),
        ("",0),
        ("A",1),
        ("AAAB",0)
    ]
    for s,k in test_cases:
        result = brute(s,k)
        result2 = optimal(s,k)
        print(f"String : '{s}', k: {k}, Longest Substring Length : {result}.")
        print(f"String : '{s}', k: {k}, Longest Substring Length using optimal: {result2}.")
if __name__ == "__main__":
    main()


