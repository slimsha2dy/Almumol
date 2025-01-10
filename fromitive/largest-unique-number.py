"""
title : Largest Unique Number
link  : https://leetcode.com/problems/largest-unique-number

description

배열 nums가 주어진다. 단 한개만 있는 가장 큰 수를 구하자.
"""
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = {}
        answer = -1
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num,count  in counter.items():
            if count == 1:
                answer = max(answer,num)
                
        return answer