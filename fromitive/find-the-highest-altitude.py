"""
title : Find the highest altitude
link  : https://leetcode.com/problems/find-the-highest-altitude

description

당신은 산에서 로드바이크를 즐기고 있다. 고도의 상대 값 배열을 gain이라고 주어질때 최대 고도 지점을 구하는 코드를 작성해야 한다.

처음 고도는 0 이다.
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentPoint = 0
        maxAltitude = 0
        for point in gain:
            currentPoint += point
            maxAltitude = max(maxAltitude,currentPoint)
        return maxAltitude
