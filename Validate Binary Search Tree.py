# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:24:09 2019

@author: ms0344303
"""

class Solution:
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root):
        return self.ValidBST(root, -9999999999, 9999999999)