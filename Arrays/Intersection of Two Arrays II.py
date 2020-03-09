"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d1 = {}
        d2 = {}
        out =[]
        for i in range(len(nums1)):
            if nums1[i] not in d1:
                d1[nums1[i]]= 1
            else :
                d1[nums1[i]] = d1[nums1[i]]+1
        for i in range(len(nums2)):
            if nums2[i] not in d2:
                d2[nums2[i]]= 1
            else :
                d2[nums2[i]] = d2[nums2[i]]+1
        d3 = {}
        if len(d1) > len(d2):
            for key  in d1.keys() :
                if key in d2 :
                    for i in range(min(d1[key],d2[key])):
                        out.append(key)
        else :
            for key in d2.keys() :
                if key in d1 :
                    for i in range(min(d1[key],d2[key])):
                        out.append(key)
        return out