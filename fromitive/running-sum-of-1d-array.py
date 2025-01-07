"""
title : Running sum of 1d array
link  : https://leetcode.com/problems/running-sum-of-1d-array

description

정수 배열 nums가 주어졌을 때 running sum은 index 0 번부터 nums 배열의 끝까지 누적합을 저장하는 배열이다.

에를 들어 nums = [1,2,3,4]일 때 running sum은 [1, 1+2, 1+2+3, 1+2+3+4] 이다.

nums가 주어졌을 때 running sum을 구하라.

풀이 해설

O(n)으로 점진적으록 누적합을 저장하면 해결된다.
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        currentSum = 0
        for num in nums:
            currentSum += num
            answer.append(currentSum)

        return answer
