# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:38:58 2019

@author: ms0344303
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(res, left, right, path):
            if left == 0 and right == 0:
                res.append(path) 
                return res
            if left > 0:
                dfs(res, left - 1, right, path + '(')
            if left < right:
                dfs(res, left, right - 1, path + ')')
        dfs(res, n, n, '')
        return res
                