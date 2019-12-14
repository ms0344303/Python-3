# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:47:52 2019

@author: ms0344303
"""
class Solution:
    def isValid(self, s: str) -> bool:
        count_s = s.count('(') - s.count(')')
        count_m = s.count('[') - s.count(']')
        count_l = s.count('{') - s.count('}')

        if count_s != 0 or count_m != 0 or count_l != 0 :
            return False
        list_s = list(s)
        enc_s = []
        for syb in list_s:
            if syb =='(':
                enc_s.append('1')
            elif syb ==')':
                 enc_s.append('-1')
            if syb =='[':
                enc_s.append('2')
            elif syb ==']':
                enc_s.append('-2')
            if syb =='{':
                enc_s.append('3')
            elif syb =='}':
                enc_s.append('-3')

        enc_s = [int(i) for i in enc_s]
        def del_axis(int_array):
            if int_array == []:
                return True
            elif len(int_array) > 2:
                for i in range(len(int_array)-1):
                    if int_array[i]+int_array[i+1] == 0:
                        return del_axis (int_array[:i]+int_array[i+2:])
                return False
        
            elif (int_array[0]*int_array[1])<0 and int_array[0]<int_array[1]:
                return False
            else:
                return True
 
        return del_axis(enc_s)