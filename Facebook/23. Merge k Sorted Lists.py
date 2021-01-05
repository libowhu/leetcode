# https://leetcode.com/problems/merge-k-sorted-lists/
# from queue import PriorityQueue
# from random import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue()
        for l in lists:
            if l: queue.put((l.val, random(), l))

        dummy = ListNode(0)
        head = dummy
        while queue.qsize():
            _, _, node = queue.get()
            head.next = node
            head = node
            if node.next:
                queue.put((node.next.val, random(), node.next))

        return dummy.next