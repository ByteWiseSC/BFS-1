"""
# Problem 1
Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
# TC : O(n) ; SC: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : return []
        dq = collections.deque()
        dq.append(root)
        result = []
    
        while dq:
            level_node = len(dq)
            node_res = []

            for _ in range(level_node):
                root = dq.popleft()
                node_res.append(root.val)

                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            
            result.append(node_res)

        return result
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS ===> TC : O(n) ; SC : O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def dfs(root, level, result):
            #base case
            if root is None: return 

            #logic
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            level += 1
            dfs(root.left, level, result)
            dfs(root.right, level, result)

        dfs(root, 0, result)
        return result
        