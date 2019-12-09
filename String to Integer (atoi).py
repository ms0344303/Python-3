# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:09:03 2019

@author: ms0344303
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        result = 0
        INTMAX =  2**31-1
        INTMIN = -2**31
        if not str or not str.strip():   #檢查是否為空字串
            return result
   
        i = 0
        while i < len(str) and str[i].isspace():  # 判斷空格
            i += 1
    
        sign = 1  # 若有‘-’則變成相反符號數
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            sign = -1
            i += 1
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            if result > (INTMAX - int(str[i])) / 10:
                return INTMAX if sign > 0 else INTMIN
            result = result * 10 + int(str[i])
            i += 1
            
        return sign * result
