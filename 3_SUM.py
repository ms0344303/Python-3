# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:44:30 2019

@author: ms0344303
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_num = len(nums)
        if len_num<3:
            return []
        sor_nums = sorted(nums)
        neg = []
        pos = []
        for i in sor_nums:
            if i <= 0:
                neg.append(i)
            else:
                pos.append(i)
        if neg ==[]:
            return []
        if all(v == 0 for v in nums):
            return [[0,0,0]]
        def search(target_list,search_list):
            res = []
            if target_list.count(0)>2:
                res.append([0,0,0])
            target_list = set(target_list)
            end = len(search_list)-1  
            for j in target_list:
                left = 0
                right = end 
                while  left < right:
                    sum_3 = j + search_list[left]+ search_list[right] 
                    if sum_3 == 0:
                        res.append([j,search_list[left],search_list[right]])
                        left = left+1
                        right = right-1
                        while left < right and search_list[left] == search_list[left - 1]:
                            left = left+1
                        while left < right and search_list[right] == search_list[right + 1]:
                            right = right-1
                    elif sum_3 < 0:
                        left = left+1
                    else:
                        right = right-1
            return res
        return search(neg,pos)+search(pos,neg)
