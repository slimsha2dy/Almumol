"""
title : Max consecutive ones III
link  : https://leetcode.com/problems/max-consecutive-ones-iii

description

1과 0으로만 이루어진 배열이 있다. 연속적으로 1의 나오는 하위 배열을 consecutive one이라고 할때 가장 긴 consecutive one을 구하자.

단! 0을 주어진 k 개수 만큼 바꿀 수 있다.

해결 방안
이전 문제를 응용하면 쉽게 풀 수 있다. 
0이 k개 보다 많아지면 줄어드는 sliding-window를 사용해보자.
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        answer = 0
        numberOfZero = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                numberOfZero += 1
            while numberOfZero > k:
                if nums[left] == 0:
                    numberOfZero -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer
