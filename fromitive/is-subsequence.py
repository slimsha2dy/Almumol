"""
title: Is subsequence
link : https://leetcode.com/problems/is-subsequence/

description

문자열 s와 t가 주어진다. s가 t의 subsequence면 true 그렇지 않으면 false를 반환한다.

subsequence란 문자가 연속으로 이어저 있지 않아도 전체 문자에 특정 문자열의 문자가 순서대로 있는 것을 말한다.

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

해결 방안

s 문자를 가리키는 포인터와 t 문자를 가리키는 포인터를 선언하여 t 문자를 순회할 때 s 문자의 포인터를 전부 체크하면 된다.

푼 이유

문자열이 포함되는 것을 two-pointer를 이용해 비교한다는게 인상적이어서 풀어보고 싶었음 크크
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPointer = 0
        tPointer = 0
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
            tPointer += 1
        
        return sPointer == len(s)
