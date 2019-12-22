# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:31:15 2019

@author: ms0344303
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0   
        for i in range(len(nums)):
            if i > reach:
                return False
            reach = max(reach, i + nums[i])
        return True
