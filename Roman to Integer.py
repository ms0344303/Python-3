# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:10:14 2019

@author: ms0344303
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} #建立Map字典
        sum = 0
        maxDigit = 1     #羅馬數字最小為1
        for i in range(len(s)-1, -1, -1):
            if digits[s[i]] >= maxDigit:  #以前後大小關係判斷是否需要相減或直接相加
                maxDigit = digits[s[i]]
                sum = sum + digits[s[i]]
            else:
                sum = sum - digits[s[i]]
        return sum