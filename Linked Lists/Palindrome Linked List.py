"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # find the middle of the list
        currentSlow = currentFast = head
        while currentFast:
            currentSlow = currentSlow.next
            if currentFast.next:
                currentFast = currentFast.next.next
            else:
                break

        # reverse second part of the list
        previous = currentSlow
        current = currentSlow.next
        previous.next = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

        # compare the front and back of the list
        currentReverse = previous
        currentForward = head
        while currentReverse and currentForward:
            if currentForward.val != currentReverse.val:
                return False
            currentReverse = currentReverse.next
            currentForward = currentForward.next

        return True


class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        pre, lens = None, 0
        h = head
        while h:
            lens += 1
            h = h.next
        if lens == 1:
            return True

        half = lens >> 1
        while half:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
            half -= 1
        if lens & 1:
            while cur and head.next:
                if cur.val != head.next.val:
                    return False
                cur = cur.next
                head = head.next
            return True
        else:
            while cur and head:
                if cur.val != head.val:
                    return False
                cur = cur.next
                head = head.next
            return True
