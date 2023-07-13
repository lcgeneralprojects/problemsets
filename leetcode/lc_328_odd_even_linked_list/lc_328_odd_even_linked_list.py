from typing import Optional
from common.singly_linked_list import stringToSLL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        cur = head
        even_head = head.next
        even_cur = even_head

        while even_cur.next is not None:
            cur.next = even_cur.next
            cur = cur.next

            if cur.next is None:
                break

            even_cur.next = cur.next
            even_cur = even_cur.next

        even_cur.next = None

        cur.next = even_head

        return head

solution_obj = Solution()

input = [1,2,3,4,5,6,7,8]
head = stringToSLL(input)

print(solution_obj.oddEvenList(head))