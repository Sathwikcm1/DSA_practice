#FIXME: Problem: Group Anagrams
#FIXME: Link: https://leetcode.com/problems/group-anagrams/
#FIXME: Given: a list of strings
#FIXME: Return: grouped list of lists — words that are anagrams go in the same group
#FIXME: Input:  ["eat","tea","tan","ate","nat","bat"]
#FIXME: Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
#FIXME: Constraints: 1 <= strs.length <= 10^4, 0 <= strs[i].length <= 100, lowercase English only
#
# Real-life example:
#   Imagine you work at a library and books arrive with scrambled title labels.
#   "eat", "tea", "ate" are all the same letters rearranged — they go on the SAME shelf.
#   You sort each label alphabetically to find which shelf it belongs to.
#   "eat" → "aet" shelf, "tan" → "ant" shelf, "bat" → "abt" shelf.
#   That's literally the optimal approach — sorted letters = shelf label = dict key.
#
# Fun fact:
#   "astronomer" is an anagram of "moon starer" 🌙
#   "listen" ↔ "silent", "dormitory" ↔ "dirty room"

from collections import defaultdict
from typing import List


class Solution:
    def is_anagram(self, s1, s2):
        return sorted(s1) == sorted(s2)

    #NOTE: Brute Force — O(n² * k log k) time, O(n) space
    #TODO: Compare every pair of strings using sorted() check, group matches with 'used' array
    #TODO: Slow because n² pair comparisons, each costing k log k for sorting
    def brute(self, strs):
        n = len(strs)
        used = [False] * n  #NOTE: tracks which strings are already grouped
        result = []
        for i in range(n):
            if not used[i]:
                group = [strs[i]]
                used[i] = True
                for j in range(i + 1, len(strs)):  #NOTE: inner loop = why it's O(n²)
                    if not used[j] and self.is_anagram(strs[i], strs[j]):
                        group.append(strs[j])
                        used[j] = True
                result.append(group)
        return result

    #NOTE: Optimal — O(n * k log k) time, O(n * k) space
    #TODO: Sort each word → use sorted tuple as dict key → anagrams share the same key
    #TODO: One pass, no pair comparisons. defaultdict auto-creates empty list for new keys.
    def optimal(self, strs):
        d = defaultdict(list)  #NOTE: defaultdict(list) → missing key auto-creates []
        for word in strs:
            key = tuple(sorted(word))  #NOTE: tuple because lists can't be dict keys (unhashable)
            d[key].append(word)
        return list(d.values())


if __name__ == "__main__":
    sol = Solution()

    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    test2 = [""]
    test3 = ["a"]

    print("--- Brute Force ---")
    print(f"Test 1: {sol.brute(test1)}")
    print(f"Test 2: {sol.brute(test2)}")
    print(f"Test 3: {sol.brute(test3)}")

    print("\n--- Optimal ---")
    print(f"Test 1: {sol.optimal(test1)}")
    print(f"Test 2: {sol.optimal(test2)}")
    print(f"Test 3: {sol.optimal(test3)}")



