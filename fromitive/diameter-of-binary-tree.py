"""
title : Diameter of Binary Tree
link  : https://leetcode.com/problems/diameter-of-binary-tree

description
binary tree가 주어졌을때 diameter(지름)을 구해야 한다. 지름이란 특정 노드 X에서 Y까지 의 경로 중 가장 긴 경로이다.

해결 방안

특정 Root 노드에서 diameter를 구하기 위해선, 왼쪽과 오른쪽의 최대 깊이를 더하면 된다. 그러나, root node를 거치지 않고 
자식 노드에서 제일 긴 경로가 나올 수 있으므로 dfs로 접근해야 한다. 
"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal answer
            left = dfs(node.left)
            right = dfs(node.right)
            answer = max(answer, left + right)
            return max(left, right) + 1
        dfs(root)
        return answer