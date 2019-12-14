# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:41:07 2019

@author: ms0344303
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        bottom = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}    
        result = []
        
        def combine(temp, left):
            if not left:
                result.append(temp)
                return 
            else:
                for char in bottom[left[0]]:
                    combine(temp + char, left[1:])
        

        combine("", digits)
        return result