# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

#Example

# Input: tree = [7,4,3,null,null,6,19], target = 3
# Output: 3
# Explanation: In all examples the original and cloned trees are shown.
# The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.


#Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Note : Here we used OR condition to check whether left subtree or the right subtree contains the target value

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         if not original:
#             return None
#
#         if original.val == target.val:
#             return cloned

#         return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right,cloned.right, target)
