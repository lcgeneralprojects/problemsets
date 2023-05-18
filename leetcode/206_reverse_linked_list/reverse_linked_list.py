# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from common.singly_linked_list import ListNode


class Solution:
    def recursionReverseList(self, prev, cur):
        next = cur.next
        cur.next = prev

        if next is None:
            return cur
        else:
            return self.recursionReverseList(cur, next)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        return self.recursionReverseList(None, head)
