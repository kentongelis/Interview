# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).


# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Solution

# 1. We can define a recursive helper function that takes two nodes as input,
# one from the left subtree and one from the right subtree.
# 2. The helper function returns true if both nodes are null, or if their values
# are equal and their subtrees are symmetric.

# Solution


class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)
