# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:55:27 2019

@author: ms0344303
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result= ''
        for element in digits:
            result += str(element)

        return  list(str(int(result)+1))