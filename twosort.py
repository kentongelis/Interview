# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together
# the nodes of the first two lists.

# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

# Solution
# 1. Use a dummy node to simplify the process of appending nodes to the merged list.
# 2. Initialize two pointers (p1 and p2) to traverse list1 and list2, respectively.
# 3. While both pointers are non-null:
#   -Compare the values at p1 and p2.
#   -Append the smaller value to the merged list and move the corresponding pointer forward.
# 4. After exiting the loop, append any remaining nodes from either list to the merged list.
# 5. Return the merged list, starting from the dummy node's next pointer.


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = prev = ListNode(0)

        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
            prev = prev.next

        if p1:
            prev.next = p1
        else:
            prev.next = p2

        return dummy.next
