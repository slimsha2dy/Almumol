"""
title : Counting Elements
link  : https://leetcode.com/problems/counting-elements

description
(별걸 다 문제로 만드네.....)

정수 배열 arr이 있을 때 arr의 원소 x 에서 x + 1가 존재하는 x의 개수를 세어야 한다. 원소는 중복될 수 있으면 중복된 원소는 각각 세어야 한다.

예를 들어, [1,2,3]이 주어졌을때 arr의 1을 기준으로 할 때 2가 있으니 count는 1이 증가해야하고 arr 2을 기준으로 할 때 arr안에 3이 존재하므로 count는 1증가해야 한다.
그래서 답은 2이다.

[1,1,2,2] 일 경우엔 1,1 각각 2,2가 있으므로 counts는 2가 된다.
"""

class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        hashTable = {}
        for x in arr:
            hashTable[x] = hashTable.get(x, 0) + 1
        for x in hashTable:
            if x + 1 in hashTable:
                counter += hashTable[x]
        
        return counter