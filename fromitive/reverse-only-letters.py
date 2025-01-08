"""
title: Reverse Only Letters
link : https://leetcode.com/problems/reverse-only-letters

description
영문 대 소문자만 뒤집도록 알고리즘을 작성하는 문제

해결 방안
1. two-pointer

left, right를 순회하면서 left혹은 right가 영문자가 나타날때까지 점점 left와 right차이를 좁혀서 뒤집는다.

2. stack
letter를 역순으로 stack 에 담는다. 
문자열 s를 순회하면서 letter이면 stack에 있는 문자를 꺼내고, 그렇지않으면 그대로 append한다.

"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) -1
        answer = [ c for c in s]
        while left < right:
            while left < len(s) and not answer[left].isalpha():
                left += 1
            while right > -1 and not answer[right].isalpha():
                right -= 1
            if left >= right:
                break
            answer[left], answer[right] = answer[right], answer[left]
            left += 1
            right -= 1
        return "".join(answer)

    def reverseOnlyLettersWithStack(self, s: str) -> str:
        stack = [ c for c in s if c.isalpha()]
        answer = []
        for c in s:
            if c.isalpha():
                answer.append(stack.pop())
            if not c.isalpha():
                answer.append(c)
        return "".join(answer)
            
