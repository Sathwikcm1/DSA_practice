#FIXME: Problem: Valid Anagram
#FIXME: Link: https://leetcode.com/problems/valid-anagram/
#FIXME: Given: Two strings `s` and `t`
#FIXME: Return: True if `t` is an anagram of `s`, else False
#FIXME: Anagram = same characters, same frequency, different order
#FIXME: Constraints:
#FIXME:   - 1 <= s.length, t.length <= 5 * 10^4
#FIXME:   - s and t consist of lowercase English letters


class Solution:
    #NOTE: Brute Force — O(n²) time, O(n) space
    #TODO: For each char in s, search for it in t. If found, remove it from t.
    #TODO: If all chars matched and t is empty → anagram.
    #TODO: Like matching socks from a pile — pick one, dig through the pile to find its pair, remove both.
    #TODO: .replace() on string creates a NEW string each time → O(n) per call × n calls = O(n²)
    def brute(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_remaining = list(t)  #NOTE: Convert to list since strings are immutable in Python
        for ch in s:
            if ch in t_remaining:
                t_remaining.remove(ch)  #NOTE: .remove() finds first occurrence and removes it — O(n) each call
            else:
                return False
        return True  #NOTE: If we matched every char in s and t_remaining is empty → anagram

    #NOTE: Better — O(n log n) time, O(n) space (Sorting approach)
    #TODO: If two strings are anagrams, sorting them both gives the SAME string.
    #TODO: "nagaram" sorted → "aaagmnr", "anagram" sorted → "aaagmnr" → MATCH!
    def better(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    #NOTE: Optimal — O(n) time, O(1) space (HashMap/Counter approach)
    #TODO: Key Insight: Anagrams have the SAME character frequency.
    #TODO: Count every char in s, then "un-count" every char in t.
    #TODO: If anything goes negative or a char in t wasn't in s → not anagram.
    #TODO: Space is O(1) because max 26 lowercase letters (fixed alphabet).
    def optimal(self, s: str, t: str) -> bool:
        if len(s) != len(t):  #NOTE: Different lengths = impossible anagram. Early return saves time.
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1  #NOTE: .get(key, default) avoids KeyError. Pythonic way to count.
        for ch in t:
            if ch not in count:  #NOTE: char in t not present in s at all → not anagram
                return False
            count[ch] -= 1
            if count[ch] < 0:  #NOTE: more of this char in t than in s → not anagram
                return False
        return True  #NOTE: Since len(s)==len(t) and no count went negative, all counts MUST be 0. No extra check needed.


#NOTE: ===== PYTHON TIPS & BUILT-INS =====
#NOTE: sorted(string) → returns list of characters in sorted order. O(n log n).
#NOTE: dict.get(key, default) → returns value if key exists, else default. No KeyError!
#NOTE: collections.Counter(s) → creates frequency dict automatically.
#NOTE:   Example: Counter("anagram") → {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
#NOTE: ONE-LINER: from collections import Counter; return Counter(s) == Counter(t)
#NOTE: But the manual approach shows interviewers you understand the LOGIC, not just the library.


if __name__ == "__main__":
    obj = Solution()

    # Case 1: Valid anagram
    s, t = "anagram", "nagaram"
    print("Case 1 (Valid):", obj.optimal(s, t))  # True

    # Case 2: Not anagram
    s, t = "rat", "car"
    print("Case 2 (Invalid):", obj.optimal(s, t))  # False

    # Case 3: Different lengths
    s, t = "abc", "ab"
    print("Case 3 (Different lengths):", obj.optimal(s, t))  # False

    # Case 4: Empty strings
    s, t = "", ""
    print("Case 4 (Empty):", obj.optimal(s, t))  # True

    # Case 5: Single character same
    s, t = "a", "a"
    print("Case 5 (Single same):", obj.optimal(s, t))  # True

    # Case 6: Single character different
    s, t = "a", "b"
    print("Case 6 (Single different):", obj.optimal(s, t))  # False

    # Case 7: With repeated letters
    s, t = "aabbcc", "abcabc"
    print("Case 7 (Repeated letters):", obj.optimal(s, t))  # True

    # Case 8: Large strings with mismatch
    s, t = "abcd" * 1000, "abce" * 1000
    print("Case 8 (Large mismatch):", obj.optimal(s, t))  # False
