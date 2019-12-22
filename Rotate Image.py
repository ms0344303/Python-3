# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:35:10 2019

@author: ms0344303
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [list(m) for m in (zip(*matrix[::-1]))]