"""
title : K radius subarray avarages
link  : https://leetcode.com/problems/k-radius-subarray-averages

description

배열 nums와 반지름 k가 주어진다. k변수는 중간 인덱스 i를 기점으로 i-k 부터 i+k를 지정하는데 쓰인다.

이때 nums 각 원소별로 중간 인덱스에 있는 평균 값을 구할 수 있으면 구하고, 불가능하다면 -1가 저장된 배열을 반환한다. 

"""
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        answer = [-1] * len(nums)
        if k * 2 > len(nums):
            return answer

        if k == 0:
            return nums
        
        currentSum = 0
        left = 0
        prefix = [ ]
        for right in range(len(nums)):
            currentSum += nums[right]
            while right - left > k * 2:
                currentSum -= nums[left]
                left += 1
            if right - left == k * 2:
                answer[k + left] = int(currentSum / (k * 2 + 1))
        return answer