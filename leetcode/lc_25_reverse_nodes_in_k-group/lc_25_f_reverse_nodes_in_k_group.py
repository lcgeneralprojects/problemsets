# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from lc_common.lc_singly_linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Better to do the following without additional functions
        # def reverseSublist(sublist_head, k):
        #     # sublist_head lies before the k-group sublist that is to be reversed
        #     curr_node = sublist_head.next
        #     for i in range(k-1):
        #         next_node = curr_node.next
        #         curr_node.next = next_node.next
        #         next_node.next = sublist_head.next
        #         sublist_head.next = next_node
        #         curr_node = curr_node.next

        super_head = ListNode()
        super_head.next = head

        counter = 0
        curr_node = super_head.next
        while curr_node:
            counter += 1
            curr_node = curr_node.next

        counter = counter // k

        curr_node = super_head
        for i in range(counter):
            sublist_head = curr_node
            curr_node = curr_node.next
            for j in range(k - 1):
                next_node = curr_node.next
                curr_node.next = next_node.next
                next_node.next = sublist_head.next
                sublist_head.next = next_node

        return super_head.next
