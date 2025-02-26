# Given the head of a linked list, remove the nth node from the end of the
# list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# Solution
# 1. Use Two Pointers:
#   - Move the first pointer n steps ahead.
#   - Then move both first and second pointers together until the first pointer
#   reaches the end.
# 2. Delete the target node:
#   - The second pointer will now be just before the node to remove.
#   - Adjust the pointers to skip the N-th node.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        first = second = dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next

        # Remove the N-th node
        second.next = second.next.next

        return dummy.next  # Return new head
