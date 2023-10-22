# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.singly_linked_list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        ptr1 = head
        ptr2 = head

        for i in range(n):
            ptr2 = ptr2.next

        if ptr2 is None:
            ptr2 = ptr1.next
            ptr1.next = None
            return ptr2

        while ptr2.next is not None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr2 = ptr1.next
        ptr1.next = ptr2.next
        ptr2.next = None

        return head
    