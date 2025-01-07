"""
title : Number of ways to split array
link  : https://leetcode.com/problems/number-of-ways-to-split-array

description

정수 배열 `nums`가 주어지고 k를 기준으로 subArray를 나눴을 때 왼쪽 subArray의 합이 오른쪽 subArray 합보다 큰 경우의 수를 구해야 한다.

풀이 방법

subArray를 나눌 때 마다 합을 계산하는 건 비효율 적이다. 그렇다면 미리 합들을 계산해놓는 prefix 방식을 채택할 수 있다.

prefix를 구하면 k에 따라 왼쪽 및 오른쪽을 배열의 합을 O(1)의 시간복잡도로 로 구할 수 있다.

left = prefix[k]
right = prefix[len(nums) - 1] - prefix[k] # 마지막 index에서 left만큼 빼면 바로 나옴


"""

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        totalSum = 0
        answer = 0 
        for index,num in enumerate(nums):
            totalSum += num
            prefix[index] = totalSum
        for index in range(len(nums) - 1):
            left = prefix[index]
            right = prefix[len(nums) - 1] - left
            if left >= right:
                answer += 1
        return answer

    def waysToSplitArrayAdvenced(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        answer = 0
        for index in range(len(nums) - 1):
            leftSum += nums[index]
            rightSum = totalSum - leftSum
            if leftSum >= rightSum:
                answer += 1
        return answer
        