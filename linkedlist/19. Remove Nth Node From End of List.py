# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head

        pre_slow = ListNode(-1)
        pre_slow.next = slow
        new_head = pre_slow

        while fast:
            fast = fast.next
            if n == 0:
                slow = slow.next
                pre_slow = pre_slow.next
            else:
                n -= 1
        pre_slow.next = pre_slow.next.next

        return new_head.next
