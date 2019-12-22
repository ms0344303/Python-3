# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:15:19 2019

@author: ms0344303
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans_line = 0
        ans_sub = 0
        seen = []
        seen_sub = []
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val != '.':
                    seen += [(val,j),(i,val)]
                if i%3 ==0 and j%3==0:
                    sub = [board[s][t] for s in [i, i+1, i+2] for t in [j, j+1, j+2]]
                    for val in sub:
                        if val != '.':
                            seen_sub += val
                    if len(seen_sub) == len(set(seen_sub)):ans_sub += 0;seen_sub = []
                    else:ans_sub += 1;seen_sub = []                  
        ans_line = len(seen) == len(set(seen))
        if ans_line == False  or ans_sub>0:return False
        else:return True