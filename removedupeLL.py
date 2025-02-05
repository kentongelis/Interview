# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Example 1
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Solution

# 1. Initialize a pointer current starting at the head of the linked list.
# 2. Traverse the list while current and current.next are not None:
#   - If current.val equals current.next.val, it means there's a duplicate. Update current.next to current.next.next to skip the duplicate.
#   - Otherwise, move the current pointer to the next node.
# 3. Once the traversal is complete, return the head of the modified list.


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:  # Handle the edge case of an empty list
            return None

        current = head  # Start traversal from the head of the list
        while current and current.next:
            if current.val == current.next.val:  # Check for duplicate
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next distinct node

        return head  # Return the modified list
