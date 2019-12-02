# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:26:49 2019

@author: ms0344303
"""

def twoSum(nums, target):    
        dict={}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]] = i
            else:
                 return [dict[target-nums[i]] ,i]