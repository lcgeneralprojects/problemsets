# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next
from typing import Optional

from common.singly_linked_list import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Floyd's Hare and Tortoise algorithm
        hare = head
        tortoise = head

        if hare is None or hare.next is None:
            return None
        tortoise = tortoise.next
        hare = hare.next.next

        # First stage
        while hare != tortoise:
            if hare is None or hare.next is None:
                return None
            tortoise = tortoise.next
            hare = hare.next.next

        # At this point, hare is at position 2x = x+k*lambda = k*lambda, where k is natural, and lambda is the length of the cycle
        # After tortoise makes mu steps from the start of the list, where mu is the 'index' of the first element in the cycle,
        # the hare will be at position k*lambda+mu = mu
        tortoise = head

        while hare != tortoise:
            tortoise = tortoise.next
            hare = hare.next

        return hare