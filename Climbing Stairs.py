# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 11:31:45 2019

@author: ms0344303
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        F_series = [1,1]
        n1 = 1
        n2 = 1

        while len(F_series) < (n+1):
            n3 = n1+n2
            n1=n2
            n2=n3
            F_nums.append(n3)
            
        return F_nums[-1]
    