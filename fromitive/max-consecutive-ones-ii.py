

"""
title : Max consecutive ones II
link  : https://leetcode.com/problems/max-consecutive-ones-ii

description

1과 0으로만 이루어진 배열이 있다. 연속적으로 1의 나오는 하위 배열을 consecutive one이라고 할때 가장 긴 consecutive one을 구하자.

단! 0을 한 번만 1로 바꿀 수 있다.

해결 방안

consecutive one은 sub Array로 생각할 수 있다. 

우리가 구하는 subArray는 [1,1,1,1,1,0] 즉, 하나의 0은 허용하는 것이다. 

따라서 [1,1,1,1,1,0,1,1,1,1]도 유효한 subArray이므로 이는 sliding-window 알고리즘을 활용해 풀 수 있다.

right 포인터를 이동시키면서 0의 개수가 2개일 경우 left를 옮겨가는 형태로 알고리즘을 풀면 된다.
"""

class Solution:
    def findMaxConsecutiveOnesII(self, nums: List[int]) -> int:
        numberOfZero = 0
        left = 0
        answer = 0
        for right in range(len(nums)):
            if nums[right] == "0":
                numberOfZero += 1
            
            while numberOfZero > 1:
                if nums[left] == "0":
                    numberOfZero -= 1
                left += 1
            answer = max(answer, right - left + 1)
        return answer