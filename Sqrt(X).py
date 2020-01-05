# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:31:45 2019

@author: ms0344303
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        
        l = 1
        r = int(x/2)
        while l <= r:
            m = l + (r - l) // 2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
            else:
                return m
        return r;