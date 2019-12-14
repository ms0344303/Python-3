# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:51:04 2019

@author: ms0344303
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length 
        
        L = 1
        left = 0 
        right= 1

        for i in range(length-1):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                left = right
                L =L+1
                right=right+1
        return L

        
