# Linked list, swap every pair of nodes and return the head
# dont modify node data only change location of nodes
# head = [1,2,3,4]
# output = [2,1,4,3]


class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        else:
            temp = head.next  # temp = 2
            head.next = self.swapPairs(
                temp.next
            )  # repeating the process on the next pair with the next node
            temp.next = head  # 2.next = 1

            return temp


# Time complexity O(n)


solution = Solution()
