# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
from lc_common.lc_singly_linked_list import ListNode
import math


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res_root = ListNode(val=-math.inf)

        # Rather inefficient. Can be solved by working over chunks (of nodes of the same value) of lists using
        # dictionaries
        # 'sll' - singly-linked list
        for list_ptr in lists:
            res_ptr_head = res_root
            res_ptr_tail = res_ptr_head.next
            sll_ptr = list_ptr
            while sll_ptr:
                if not res_ptr_tail or sll_ptr.val < res_ptr_tail.val:
                    res_ptr_head.next = sll_ptr
                    sll_ptr = sll_ptr.next
                    res_ptr_head = res_ptr_head.next
                    res_ptr_head.next = res_ptr_tail
                else:
                    res_ptr_head = res_ptr_tail
                    res_ptr_tail = res_ptr_tail.next

        return res_root.next
