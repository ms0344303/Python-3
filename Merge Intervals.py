# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:05:05 2019

@author: ms0344303
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []
        for  i in range(len(intervals)):
            if res==[]:
                res.append(intervals[i])
            else:
                if res[-1][0]<= intervals[i][0] <= res[-1][1]:
                    res[-1][1] = max(intervals[i][1],res[-1][1])
    
                else:
                    res.append(intervals[i])
        return res