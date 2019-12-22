# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:31:48 2019

@author: ms0344303
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        for word in strs:
            word_key = "".join(sorted(word))
            if word_key not in temp_dict:
                temp_dict[word_key] = [word]
            else:
                temp_dict[word_key].append(word)

        result =[]
        result += [value for value in temp_dict.values()] 
        return result