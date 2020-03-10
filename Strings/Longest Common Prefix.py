"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs)==0):
            return ""
        else:
            lengths = []
            for i in strs:
                lengths.append(len(i))

            output = []
            for i in range(min(lengths)):
                temp = [s[i] for s in strs]
                if(all(x==temp[0] for x in temp)):
                    output.append([temp[0]])
                else:
                    break

            string = ""
            for i in output:
                for j in i:
                    str1 = ''.join(j)
                string += str1

        return string