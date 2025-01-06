"""
title : Subarray sum equals k
link  : https://leetcode.com/problems/subarray-sum-equals-k

description

정수를 담은 nums 배열이 있다. 하위 배열의 합 k를 만족하는 하위 배열의 개수를 구해야 한다.

해결 방안

정렬도 되어있지 않아 sliding window로 해결이 쉽지 않다. 문제를 해결하기 위해선 모든 subArray의 합을 구하는 방법이 있다고 만 생각했다.

sliding window를 사용하기 위해선 배열의 시작과 끝을 각각 left right 포인터로 만들고, 이를 이용해 탐색하면 된다.

그러나, 이 문제 같은 경우엔 어느 조건에 left와 right를 움직어야 하는지 감이 잡히지 않았다.

무작위 대입법으로 풀어봤지만, 시간초과 대답이 나왔다.

그래서 답변을 보니 다른 관점으로 접근하는 것을 보았다.

포인터 i,j는 각각 0 부터 i까지의 합, 0부터 j까지의 합을 나타낸다고 정의할 때 k를 구하는 과정은 아래와 같은 식을 작성할 수 있다. 단 (j <= i)

```
sum[i] - sum[j] = 또다른 subArray
```

위의 표현방식으로 sum[i] - sum[j] = k 를 만족하는 sum의 개수를 구한다.

**여기서 중요한 포인트는** sum이 가능한 배열을 구하기 쉽다.

순차적으로 nums에 있는 숫자를 더하기만 하면 된다.

따라서 sum[i] - k = sum[j]를 만족하는 j를 구하는 것이 k를 구하는 것과 동일하기 때문에 

아래와 같이 시간복잡도가 O(n), 공간복잡도가 O(n)인 해결방안이 나올 수 있게 된 것이다.
"""

class Solution:
    # 시간초과
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        for left in range(len(nums)):
            currentSum = 0
            for right in range(left,len(nums)):
                currentSum += nums[right]
                if currentSum == k:
                    answer += 1 
        return answer

    def advencedsubArraySum(self, nums: List[int], k: int) -> int:
        memoizedMap = {0 : 1}
        currenSum = 0
        answer = 0 
        for start in range(len(nums)):
            currentSum += nums[start]
            if currentSum - k in memoizedMap:
                answer += memoizedMap[currentSum - k]
            memoizedMap[currentSum] = memoizedMap.get(currentSum, 0) + 1
        
        return answer
