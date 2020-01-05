# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 08:01:27 2019

@author: ms0344303
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        cnt_0 = nums.count(0)
        cnt_1 = nums.count(1)
        cnt_2 = nums.count(2)
        for i in range(len(nums)):
            if i < cnt_0:
                nums[i] = 0
            elif i < cnt_0 + cnt_1:
                nums[i] = 1
            else:
                nums[i] = 2
