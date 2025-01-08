"""
title : Minimum Size Subarray Sum
link  : https://leetcode.com/problems/minimum-size-subarray-sum

description

nums 배열이 주어졌을 때 subarray의 합이 target k 보다 크거나 같은 만족하는 subarray의 최소 길이를 구해야 한다.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        answer = 0
        currentSum = 0 
        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                if answer == 0:
                    answer = right - left + 1
                answer = min(answer, right - left + 1)
                currentSum -= nums[left]
                left += 1
        return answer