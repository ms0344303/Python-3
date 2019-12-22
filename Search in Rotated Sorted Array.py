# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 07:59:01 2019

@author: ms0344303
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: 
            return  -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1