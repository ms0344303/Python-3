# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 08:47:09 2019

@author: ms0344303
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def empty(seq):
            try:
                return all(map(empty, seq))
            except TypeError:
                return False
        if empty(matrix):
            return []
        if len(matrix)==1 or len(matrix[0]) ==1:
            flat_list = []
            for sublist in matrix:
                for item in sublist:
                    flat_list.append(item)
            return flat_list
        length = len(matrix)
        width = len(matrix[0])
        up = matrix[0]
        matrix[length-1].reverse()
        down =  matrix[length-1]
        left = [i[0] for i in matrix[1:length-1]][::-1]
        right = [i[width-1] for i in matrix[1:length-1]]
        
        return  up+right+down+left+self.spiralOrder([item[1:len(matrix[0])-1] for item in matrix[1:len(matrix)-1]])
