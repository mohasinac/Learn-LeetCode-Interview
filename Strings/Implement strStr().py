"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        if n<1 or needle==haystack:
            return 0
        if h<1:
            return -1
        
        for i, c in enumerate(haystack):
            if c==needle[0] and (i+n)<=h and all([haystack[i+j]==needle[j] for j in range(1,n)]):
                return i 
        
        return -1
                