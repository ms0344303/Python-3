# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:56:58 2019

@author: ms0344303
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        sum_p,sum_m,sum_n =1,1,1
        
        p = m+n-2
        for i in range(1,p+1):
            sum_p = sum_p*i
        for j in range(1,m):
            sum_m = sum_m*j
        for j in range(1,n):
            sum_n = sum_n*j
            
        return int(sum_p/(sum_m*sum_n))
            