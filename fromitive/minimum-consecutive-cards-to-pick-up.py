""" 
title : Minimum consecutive cards to pick up
link : https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

description

숫자가 적힌 카드 배열 cards가 있다. cards를 순서대로 뽑아서 적어도 하나의 짝이 맞는 카드를 가질 수 있는 최소 뽑기 수를 구해야 한다.  

예를 들어 [1,2,3,4,2,4,1] 일 경우 정답은 3이다. 4,2,4를 뽑을 때 4가 짝이 맞는 카드이다. 

해결 방안

카드를 순서대로 뽑으면서 각 카드의 인덱스 값을 기록해 놓고, 최소값을 구한다.
"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        counter = {}
        answer = float("inf")
        for right in range(len(cards)):
            if cards[right] in counter:
                answer = min(answer, right - counter[cards[right]] + 1)
            counter[cards[right]] = right
        return answer if answer < float('inf') else -1