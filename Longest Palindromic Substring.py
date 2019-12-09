# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:06:59 2019

@author: ms0344303
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < lenS:
            if lenS - i <= maxLen / 2: break   #長度低於記錄中的最長者一半時，不可能超越
            else:
                j, k = i, i   #J:暫時起點  K:暫時終點
                while k < lenS - 1 and s[k] == s[k + 1]: k += 1  #逐字檢查是否為偶數對稱
                i = k + 1   #更新i 不重複搜索
                while k < lenS - 1 and j  and s[k + 1] == s[j - 1]:  k, j = k + 1, j - 1         #再檢查是否為奇數對稱
                if k - j + 1 > maxLen: minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]