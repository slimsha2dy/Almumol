"""
title : Reverse words in a string III
link  : https://leetcode.com/problems/reverse-words-in-a-string-iii

description

문자 배열 `s`가 주어질 때 공백으로 구분된 단어들을 전부 뒤집는 알고리즘을 작성해보자.


예제 1 
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

예제 2
Input: s = "Mr Ding"
Output: "rM gniD"

해결 방안

정말 간단하게 split 하고 two-pointer를 사용해서 각 단어들의 문자를 뒤집는다.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split()])