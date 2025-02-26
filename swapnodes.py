# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]

# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

# Solution
# Base case: The list is empty or includes one node. In both cases head is a
# valid output.
# General case: The head next node will be the rest of the list (the list the
# recursive call returns) and we make the second node of the pair points to
# the head while return it as the new head.


class Solution(object):
    def swapPairs(self, head):
        if None == head or None == head.next:
            return head
        else:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head

            return temp
