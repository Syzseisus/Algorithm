# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[2, 2, 5, null, null, 5, 7]
TreeNode{val: 2, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 5, left: TreeNode{val: 5, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}

[1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]
TreeNode{val: 1, left: TreeNode{val: 1, left: TreeNode{val: 1, left: TreeNode{val: 3, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}, right: TreeNode{val: 1, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 6, left: None, right: None}}}, right: TreeNode{val: 1, left: TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 1, left: None, right: None}}, right: TreeNode{val: 1, left: None, right: None}}}, right: TreeNode{val: 3, left: TreeNode{val: 3, left: TreeNode{val: 3, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}, right: TreeNode{val: 4, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}}
1
1             3
1       1     3   4 
3   1   1   1 3 8 4 8
3 3 1 6 2 1
"""
# 이렇게 풀면 안되는데...
from collections import deque
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # 모든 노드 다 저장
        vals = set([root.val])
        nodes = deque([root])
        while nodes:
            node = nodes.popleft()
            if node.left is None:
                continue
            vals.add(node.left.val)
            vals.add(node.right.val)
            nodes.append(node.left)
            nodes.append(node.right)

        # sort 해서
        vals = sorted(vals)
        # 하나면 -1
        if len(vals) == 1:
            return -1
        # 더 있으면 두 번째로 작은 거 반환
        else:
            return vals[1]