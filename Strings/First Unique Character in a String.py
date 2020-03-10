"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen :
                seen[s[i]] = 1
            else :
                seen[s[i]] += 1
        
        for key in seen.keys():
            if seen[key]==1:
                return s.index(key)
        return -1
        
