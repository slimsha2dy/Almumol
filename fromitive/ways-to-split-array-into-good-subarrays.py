"""
title : Ways to Split Array Into Good Subarrays
link  : https://leetcode.com/problems/ways-to-split-array-into-good-subarrays

description

0과 1로 이루어진 nums 배열이 주어진다. 정확히 1이 한개 포함되는 subArray로 나누는 방법의 수를 구해야 한다.

해결 방안

예를 들어 [0,1,0,1,1,0,1,0] 있다고 가정하자.

정확히 1이 각각의 subArray로 나누는 방법의 수 중 간단한 방법은 1이 보일때 마다 쪼갤 수 있다는 것이다.
[01|01|10|10] 이런식으로 말이다.

나눌 수 있는 방법의 수는 1과 1사이의 0의 개수만큼 의존적이다.
Input: nums = [0,1,0,0,1]
Output: 3
Explanation: There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]

즉 오른쪽 1의 index에서 왼쪽 1 index를 빼면 방법의 개수가 나온다.

그럼 [0,1,0,0,1,0,1] 로 주어졌을때 경우의 수는 어떻게 구할 것인가? 결론부터 이야기하자면 [0,1,0,0,1]의 방법의 수 * [1,0,1]의 방법의 수이다.
왼쪽의 1 뒤에있는 수나, 오른쪽 1 앞에 있는 수는 경우의 수에 영향을 주지 않기 때문이다. [1,1,0,1,1]이렇게 있어도 [1|1,0,1|1]로 나누어버리면 그만이니까 말이다.
따라서 1의 개수를 점진적으로 더하는 Prefix 혹은, sliding-window로 누적합을 구해 해결이 가능하다.
"""


class Solution:
    def numberOfGoodSubarraySplitsWithPrefix(self, nums: List[int]) -> int:
        answer = 1
        counter = {}
        currentSumOfOne = 0
        counter[0] = 1
        for right in range(len(nums)):
            currentSumOfOne += nums[right]
            if nums[right] == 1 and currentSumOfOne - 1 in counter:
                answer = (answer * (right - counter[currentSumofOne - 1])) % (10 ** 9 + 7)
                counter[currentSumOfOne] = right
        if 1 not in counter:
            return 0
        return answer
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        answer = 1
        counter = {}
        left = 0
        for right in range(len(nums)):
            if nums[right] == 1 and 1 in counter:
                left = counter[1]
                answer = (answer * (right - left)) % (10 ** 9 + 7)
            counter[nums[right]] = right
        if 1 not in counter:
            return 0
        return answer