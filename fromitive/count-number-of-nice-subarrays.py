"""
title : Count Number of Nice Subarrays
link  : https://leetcode.com/problems/count-number-of-nice-subarrays

description

정수 배열 nums와 정수 k가 주어질 때 홀수 개수가 k인 subarray의 총 합을 구해야 한다.

해결 방안

subarray-sum-equals-k와 비슷한 문제이다. 

탐색하는 Nums의 인덱스를 증가시키면서 Subarray의 개수를 구해야 한다.

이때 subarray안의 홀수 개수를 기록하기 위해 해시맵을 사용한다.

해시맵의 Key를 현재 홀수의 개수로 지정하고, value는 존재하지 않을 경우 +1 을 한다. 

key - k 를해서 counter를 조회하는데 성공하면 answer에 누적한다. 

그 이유는 현재 counter는 누적해서 홀수 개수를 적재하므로 현재 홀수 개수 - k = 이전 subarray가 나온다면 현재 - 이전 = 홀수가 k개인 subArray를 구할 수 있게 된다.

"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counter = {}
        right = 0 
        answer = 0
        counter[0] = 1
        for num in nums:
            right += num % 2
            answer += counter.get(right - k, 0)
            counter[right] = counter.get(right, 0) + 1
        return answer