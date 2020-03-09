"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-(1)] =  (digits[-(1)] + carry + 1 )
        if(digits[-1]> 9):
            carry = 1
            digits [(-1)]= digits[-1] %10
        
        else :
            carry =0
        
        for i in range(1,len(digits)):
            digits[-(i+1)] =  digits[-(i+1)] + carry 
            if(digits [(-i-1)]>9):
                carry = 1  
                digits [(-i-1)] = digits [(-i-1)] %10
            else :
                carry = 0
            
        if(carry > 0 ):
            digits = [carry] + digits 
            
        return digits