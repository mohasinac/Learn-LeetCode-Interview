"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)

        if l1 is None:
            return l2

        if l2 is None:
            return l1
        curr = head
        while(l1 is not None and l2 is not None):
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            print(str(curr.val)+"both while")
            curr = curr.next

        while(l1 is not None):
            curr.next = l1
            curr = curr.next
            l1 = l1.next
            print(str(curr.val)+"in l1 while")
        while(l2 is not None):
            curr.next = l2
            curr = curr.next
            l2 = l2.next
            print(str(curr.val)+"in l2 while")

        return head.next
