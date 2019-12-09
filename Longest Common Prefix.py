# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:11:41 2019

@author: ms0344303
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):     #逐個字母掃描
            for j in range(1, len(strs)): #逐個單字掃描，如發現不再重複立刻中止並返回值
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:   #先檢測單字長度是否超過後續在檢查一致性
                    return res
            res = res + strs[0][i]
        return res

