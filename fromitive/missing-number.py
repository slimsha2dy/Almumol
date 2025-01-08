"""
title : Missing Number
link  : https://leetcode.com/problems/missing-number

description

nums는 0부터 n까지의 수 중 숫자 하나가 없는 배열이다. 배열에서 존재하지 않은 수를 찾아라.

해결 방안
1부터 n까지 더한 수에서 0 부터 n 까지 더한 수를 빼면 결과가 나온다.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = int((n * (n + 1))/ 2) 
        return totalSum - sum(nums)
