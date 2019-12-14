# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:59:01 2019

@author: ms0344303
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return  [-1,-1]
        num_l = len(nums)
        if num_l == 1:
            if nums[0] == target: return [0,0]
            else : return [-1,-1]
        left, right = 0, num_l - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                    ans_l,ans_r = mid,mid
                    while ans_l-1>=0 and nums[ans_l-1] == nums[mid]:
                        ans_l = ans_l-1
                    while ans_r+1 < num_l  and nums[ans_r+1]== nums[mid]:
                        ans_r = ans_r+1
                    return [ans_l,ans_r]

            if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
            else:
                    right = mid - 1
        return  [-1,-1]