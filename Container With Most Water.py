# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:09:28 2019

@author: ms0344303
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        MaxArea = min(height[left],height[right])*(right-left)

        while left < right:
            if height[left]<height[right]:
                left = left+1
            else:
                right = right -1
            newArea = min(height[left],height[right])*(right-left)
            MaxArea = max(MaxArea,newArea)

        return MaxArea