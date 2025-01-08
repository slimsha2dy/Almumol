"""
title : Intersection of Multiple Arrays
link  : https://leetcode.com/problems/intersection-of-multiple-arrays

description

2차원 배열이 주어지고, 각 배열들은 중복 없는 숫자들로 이루어져있다. 이때 모든 배열들에 공통되게 포함되어 있는 숫자를 찾고 정렬해야 한다.

"""

class Solution:
    def intersection(self, numsArray: List[List[int]]) -> List[int]:
        counter = {}
        for nums in numsArray:
            for num in nums:
                counter[num] = counter.get(num, 0) + 1
    
        answer = []
        for num in counter:
            if counter[num] == len(numsArray):
                answer.append(num)
        
        return sorted(answer)
