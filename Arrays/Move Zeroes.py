"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        cur = 0
        while (cur < len(nums)):
            if (nums[cur] != 0):
                
                temp = nums [lastNonZeroFoundAt]
                nums [lastNonZeroFoundAt] = nums[cur]
                nums[cur] = temp
                lastNonZeroFoundAt += 1
            cur +=1 