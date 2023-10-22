# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from lc_common.lc_singly_linked_list import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head.next = head
        curr = head

        while curr.next and curr.next.next:
            node_1 = curr.next
            node_2 = node_1.next

            node_1.next = node_2.next
            node_2.next = node_1
            curr.next = node_2
            curr = node_1

        return head.next
