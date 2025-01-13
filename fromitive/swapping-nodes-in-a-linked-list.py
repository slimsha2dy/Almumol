"""
title : Swapping Nodes in a Linked list
link  : https://leetcode.com/problems/swapping-nodes-in-a-linked-list

description
시작 지점에서 k 번째의 Node와 마지막 지점부터 뒤로 k 번째 Node의 값을 바꾸는 코드를 작성해야 한다.
"""
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(k - 1):
            fast = fast.next
        begin = fast
        fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        end = slow
        tmp = begin.val
        begin.val = end.val
        end.val = tmp
        return head
        