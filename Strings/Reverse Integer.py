"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""
class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        sign = -1 if x < 0 else 1
        x = x*sign
        while (x!=0):
            pop=x%10
            x=x//10

            if (rev > 2147483647/10) or (rev==2147483647/10 and pop >7):
                return 0
            if (rev <-2147483648/10) or (rev==-2147483648/10 and pop <-8):
                return 0
            temp=rev*10+pop
            rev=temp

        return(rev*sign)