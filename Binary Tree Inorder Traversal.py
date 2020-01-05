# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:24:09 2019

@author: ms0344303
"""

class Solution(object):
    def inorderTraversal(self, root):

        answer = []
        def inorder(root):
            if root == None:
                return None
            if root.left != None:
                inorder(root.left)
            answer.append(root.val)
            if root.right != None:
                inorder(root.right)
        inorder(root)
        return answer