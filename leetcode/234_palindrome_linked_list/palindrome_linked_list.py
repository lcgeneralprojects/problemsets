# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.singly_linked_list import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Accepting side effects for the sake of an O(1) space solution

        left = head
        right = head

        # Finding the middle
        # right will end up pointing at nothing for a list with an even amount of nodes,
        #   and at the last element for a list with an odd amount of nodes
        # left will end up pointing at the first node in the end-half of a list with an even amount of nodes,
        #   and at the middle for a list with an odd amount of nodes
        while right and right.next:
            left = left.next
            right = right.next.next

        # Inverting the right half
        mem1 = None
        while left is not None:
            mem2 = left
            left = left.next
            mem2.next = mem1
            mem1 = mem2

        # Going through the list again
        left = head
        right = mem1

        while right is not None:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
    