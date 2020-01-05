# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 08:16:16 2019

@author: ms0344303
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        Sign_C= 0
        Sign_R= 0
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] == 0:
                Sign_C = 1 

        for j in range(n):
            if matrix[0][j] == 0:
                Sign_R = 1 
       
        for k in range(1,m):
            for l in range(1,n):
                if matrix[k][l] == 0:
                    matrix[k][0] = matrix[0][l] = 0
        for o in range(1, m):
            for p in range(1, n):
                if matrix[0][p] == 0 or matrix[o][0] == 0:
                    matrix[o][p] = 0


        if Sign_C ==1 :
            for i in range(m):
                matrix[i][0] = 0
        if Sign_R ==1:
            for j in range(n):
                matrix[0][j] = 0


