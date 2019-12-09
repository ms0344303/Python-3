# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:03:44 2019

@author: ms0344303
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        a={}   #創建字典
        count=0   #相異字橫跨位數
        first=-1  #首個相異字組的位置
        for i in range(len(s)):
            if s[i] in a and a[s[i]]>first:   #判斷新字母是否出現過且是否是最新的位置
                first=a[s[i]]                 #更新首個字組的位置
            a[s[i]]=i
            count=max(count,(i-first))
        return count