# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:07:52 2019

@author: ms0344303
"""

class Solution:
    def reverse(self, x: int) -> int:
        def getreverse(input):
            str_int = str(input)
            rev = []
            len_str=len(str_int)
            for i in range(len_str):
                rev.append (str_int[len_str-i-1])
            j = 0
            while j < len_str and int(rev[0])==0:
                rev = rev[1:]
                j = j+1

            return int([''.join(rev[:])][0])

        if  x ==0:
            return  0
        elif x<0:
            ans = -1*getreverse(abs(x))
        else:
            ans =   getreverse(abs(x))
        if ans > (2**31)-1 or ans < -(2**31):
            return  0
        else:
            return ans   