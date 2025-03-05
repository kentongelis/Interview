# Given the roots of two binary trees p and q, write a function to check if they
# are the same or not.

# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.


# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false

# Solution

# 1.Check the base case: if both trees are null, return true.
# 2. Check if only one tree is null or the values of the current nodes are different, return false.
# 3. Recursively check if the left subtrees of both trees are identical.
# 4. Recursively check if the right subtrees of both trees are identical.
# 5. Return the logical AND of the results from steps 3 and 4.


class Solution:
    def isSameTree(self, p, q):
        # If both nodes are None, they are identical
        if p is None and q is None:
            return True
        # If only one of the nodes is None, they are not identical
        if p is None or q is None:
            return False
        # Check if values are equal and recursively check left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Values are not equal, they are not identical
        return False
