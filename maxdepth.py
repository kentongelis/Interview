# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Solution
# 1. Use a post order traversal and visit the current node after you calculated
# the left and right depths:

#   - At each node, recursively calculate the maximum depth of its left and
#     right children.
#   - Add 1 to account for the current node.
#   - The base case occurs when we reach a null node (leaf node's child),
#     returning 0.

# Solution


def maxDepth(self, root) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
