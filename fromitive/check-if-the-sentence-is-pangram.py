"""
title : Find the highest altitude
link  : https://leetcode.com/problems/check-if-the-sentence-is-pangram

description
한 문자열 s에 a부터 z까지 적어도 한개가 포함되어 있는 것을 pangram이라고 한다.
pangram을 구하는 코드를 작성해보자.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = [0] * 26
        for character in sentence:
            alphabet[ord(character) - ord('a')] += 1

        for counter in alphabet:
            if counter == 0:
                return False
        return True
