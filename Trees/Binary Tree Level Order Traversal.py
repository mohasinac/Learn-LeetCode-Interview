"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]
        while True:
            path = []
            while stack:
                path.append(stack.pop())
            for i in range(len(path)-1, -1, -1):
                if path[i].right:
                    stack.append(path[i].right)
                if path[i].left:
                    stack.append(path[i].left)
                path[i] = path[i].val
            if not path:
                break
            res.append(path)
        return res
