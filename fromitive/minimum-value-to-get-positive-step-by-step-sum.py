"""
title : Maximum Average Subarray I
link  : https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum

description

0보다 큰 정수 startValue와 배열 nums가 주어질 때, nums 의 배열을 왼쪽부터 더하여 항상 양의 정수가 나오는 최소 startValue를 구해야 한다.

해결 방안

prefix를 만들면 해당 prefix의 최소값이 나온다. 이 최소값이 음수일 경우 양수가 되기위한 + 1을 붙이면 startValue를 구할 수 있다.

모든 nums의 원소가 양수일경우 startValue의 최소값인 1을 반환한다.
"""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        currentSum = 0
        for index in range(len(nums)):
            currentSum += nums[index]
            prefix[index] = currentSum
        if min(prefix) < 0:
            return abs(min(prefix)) + 1
        return 1