# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:19:50 2019

@author: ms0344303
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(elements):
            if len(elements) > 0:
                head = elements[0]
                for tail in powerset(elements[1:]):
                    yield [head] + tail
                    yield tail
            else:
                yield []
        
        return list(powerset(nums))       