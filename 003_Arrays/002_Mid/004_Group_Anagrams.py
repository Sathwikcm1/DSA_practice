class Solution: 
    def is_anagram(self,s1,s2): 
        return sorted(s1) == sorted(s2)

    def brute(self,strs):
        n = len(strs)
        used = [False] * n
        result = []

        for i in range(n): 
            if not used[i]:
                group = [strs[i]]
                used[i] = True
                for j in range(i+1,len(strs)): 
                    if not used[j] and self.is_anagram(strs[i],strs[j]):
                        group.append(strs[j])
                        used[j] = True
                result.append(group)
        return result
