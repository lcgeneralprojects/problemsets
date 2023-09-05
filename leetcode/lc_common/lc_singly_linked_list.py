class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listToSLL(input):
    if input == '' or input == []:
        return None

    head = ListNode(input[0])
    cur = head

    for value in input[1:]:
        next = ListNode(value)
        cur.next = next
        cur = next

    return head

def SLLToList(input):
    res = []
    cur = input

    while cur is not None:
        res.append(cur.val)
        cur = cur.next

    return res

