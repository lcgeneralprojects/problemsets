from typing import Optional
from common.singly_linked_list import *


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge sort solution

        # Split the list
        def split(head):

            slow = head
            fast = head.next

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            fast = slow.next
            slow.next = None

            return head, fast

        # Merge the lists
        def merge(head_1, head_2):

            if head_1.val < head_2.val:
                head_merged = head_1
                cur_merged = head_merged
                cur_1 = head_1.next
                cur_2 = head_2
            else:
                head_merged = head_2
                cur_merged = head_merged
                cur_1 = head_1
                cur_2 = head_2.next

            while cur_1 is not None and cur_2 is not None:
                if cur_1.val < cur_2.val:
                    cur_merged.next = cur_1
                    cur_merged = cur_merged.next
                    cur_1 = cur_1.next
                else:
                    cur_merged.next = cur_2
                    cur_merged = cur_merged.next
                    cur_2 = cur_2.next

            if cur_1 is None:
                cur_merged.next = cur_2
            else:
                cur_merged.next = cur_1

            return head_merged

        # Main body
        if head is None or head.next is None:
            return head

        left, right = split(head)
        left, right = self.sortList(left), self.sortList(right)
        res = merge(left, right)

        return res
