#!/usr/bin/env python3

"""
title : Reverse String
link  : https://leetcode.com/problems/reverse-string

description

문자 배열 `s`가 주어질 때 배열의 순서를 뒤집는 알고리즘을 작성한다. 

해결 방안

two-pointer를 활용하여 해결하였다.

two-pointer를 사용하기 위해선 3가지 고민포인트가 필요하다.

1. left pointer의 index 값
2. right pointer의 index 값
3. 루프 종료 시점

reverse가 끝나는 시점은 두 포인터가 이미 탐색한 지점을 만나게 될 때 종료한다.
즉 left가 right 값을 넘어서는 순간 이미 탐색한 element 이므로 종료가 되는 것이다.

"""      

class Solution:
    def reverseString(self, strings: List[str]) -> None:
        left = 0
        right = len(strings) - 1

        while left < right:
            strings[left], strings[right] = strings[right], strings[left]
            left += 1
            right -= 1

        return strings

if __name__ == "__main__":
    solution = Solution()
    answer = ['a','b','c','d','e','a']
    result = solution.reverseString(['a','e','d','c','b','a'])
    assert answer == result
