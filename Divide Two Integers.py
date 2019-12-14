# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:50:00 2019

@author: ms0344303
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
   
        a = abs(dividend) 
        b =  abs(divisor)
        if a < b:
            return 0

        quo = 0
        while a >= b:
            temp_divisor = b
            temp_quo = 1
            while temp_divisor+temp_divisor < a:
                temp_divisor = temp_divisor+temp_divisor
                temp_quo = temp_quo+temp_quo
            a = a-temp_divisor
            quo = quo+temp_quo
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            quo = -quo
            
        if quo > (2**31-1) or quo < -(2**31):
            return 2**31-1
        return quo
        