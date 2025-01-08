"""
title : Longest Substring Without Repeating Characters
link  : https://leetcode.com/problems/longest-substring-without-repeating-characters

description

문자열 s를 주어졌을 때 알파벳이 중복되지 않은 가장 긴 substring를 구하자

해결 방안

전통 sliding-window로 구하는 방법과 건너뛰는 응용 방법이 있다.

중복된 알파뱃의 인덱스를 바로 찾을 수 있다면 반복문을 통해 left를 한칸씩 이동하지 않아도 가능하다.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        counter = {}
        answer = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while counter[s[right]] > 1:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
        return answer

    def lengthOfLongestSubstringII(self, s: str) -> int:
        left = 0
        charIndexTable = {}
        answer = 0
        for right in range(len(s)):
            # 슬라이딩 윈도우의 조건까지 넣어야 한다.
            if s[right] in charIndexTable and charIndexTable[s[right]] >= left:
                left = charIndexTable[s[right]] + 1
            charIndexTable[s[right]] = right
            answer = max(answer, right - left + 1)
        return answer
