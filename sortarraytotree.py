# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.


# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

# Solution

# As array is sorted, we will simply take mid as root and then find the further roots
# as recursion goes forward and then return the Root


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        def Build(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = Build(start, mid - 1)
            root.right = Build(mid + 1, end)

            return root

        return Build(0, len(nums) - 1)
