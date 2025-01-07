"""
title : Maximum Average Subarray I
link  : https://leetcode.com/problems/maximum-average-subarray-i.py

description

길이가 k인 contiguous subArray의 평균 최대값을 구해야 한다.

해결 방안
O(n)으로 풀기 위해 sliding-window를 쓸 수 있다.
k 개수가 고정되어 있고 window size가 k 보다 커지면 left를 움직인다.
answer에는 nums에 음수값이 포함되어 있으니 최소 입력값을 넣는다.

k 개수가 고정되어 있으니, 유동적인 sliding-window 기법을 사용하지 않아도 풀 수 있다.
"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        answer = - 10 ** 4 # minimum range
        totalSum = 0
        for right in range(len(nums)):
            totalSum += nums[right]
            while right - left > k - 1:
                totalSum -= nums[left]
                left += 1
            if right - left == k - 1:
                answer = max(answer, totalSum / k)
        return answer

    def findMaxAverageII(self, nums: List[int], k: int) -> float:
        sumTable = [0] * len(nums) + 1
        totalSum = 0
        for index, num in enumerate(nums):
            totalSum += num
            sumTable[index + 1] = totalSum
        answer = sumTable[k] / k # k <= len(nums)

        for index in range(k, len(nums) + 1):
            average = (sumTable[index] - sumTable[index - k]) / k
            answer = max(ansewr, average)
        
        return answer
