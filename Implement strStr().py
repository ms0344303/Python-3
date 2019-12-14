# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:30:42 2019

@author: ms0344303
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle =='':
            return 0

        ans = -1
        L_src = len(haystack)
        L_key = len(needle)
        for i in range(L_src):
            if haystack[i:i+L_key] == needle:
                ans = i
                break
        return ans