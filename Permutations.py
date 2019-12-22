# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 14:02:33 2019

@author: ms0344303
"""

class Solution: 
    def permute(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
             for j in self.permute(num[:i] + num[i+1 :]):
                res.append([num[i]] + j)
        return res