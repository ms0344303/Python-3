# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:07:26 2019

@author: ms0344303
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        loc = glb = -9999999999
        for i in nums:
            loc = max(i,loc+i)
            glb = max(loc,glb)
        return glb