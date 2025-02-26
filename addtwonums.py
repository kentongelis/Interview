# You are given two non-empty linked lists representing two non-negative integers. The digits
# are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Solution
# 1. Use a dummy node to simplify result list construction.
# 2. Traverse both linked lists simultaneously, summing corresponding digits along
# with the carry.
# 3. Create new nodes for the result linked list, using the least significant digit
# of the sum.
# 4. Update the carry for the next iteration.
# 5. Continue until all nodes in both lists and the carry are processed.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()  # Initialize the dummy node
        current = dummy  # Pointer to build the result list

        # Single unified loop for l1, l2, and carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)  # Add new node with the digit
            current = current.next

            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
