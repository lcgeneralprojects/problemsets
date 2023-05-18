# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.singly_linked_list import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        point_1 = head
        point_2 = head

        while point_1:
            if i % 2 == 1:
                point_2 = point_2.next

            point_1 = point_1.next
            i += 1

        return point_2
