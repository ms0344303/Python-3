# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:24:09 2019

@author: ms0344303
"""

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        self.dfs(root, 0, ans)
        return ans

    def dfs(self, root, depth, res):
        if root == None:
            return res
        if len(res) < depth+1:
            res.append([])
        if depth %2 == 0:
            res[depth].append(root.val)
        else:res[depth].insert(0,root.val)
        self.dfs(root.left, depth+1, res)
        self.dfs(root.right, depth+1, res)