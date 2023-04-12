# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        carry = 0
        curNode = res
        prevNode = res
        while True:
            if l1 is not None:
                a = l1.val
                l1 = l1.next
            else:
                a = 0

            if l2 is not None:
                b = l2.val
                l2 = l2.next
            else:
                b = 0

            if a + b + carry == 0 and l1 is None and l2 is None:
                prevNode.next = None
                break
            else:
                curNode.val = a + b + carry

            if curNode.val > 9:
                carry = 1
                curNode.val -= 10
            else:
                carry = 0

            curNode.next = ListNode()
            prevNode = curNode
            curNode = curNode.next

        return res
