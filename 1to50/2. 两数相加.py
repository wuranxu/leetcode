# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(-1)
        ans = node
        one = False
        while l1 is not None and l2 is not None:
            result = l1.val + l2.val + (1 if one else 0)
            one = result >= 10
            temp = ListNode(result % 10)
            node.next = temp
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            result = l1.val + (1 if one else 0)
            one = result >= 10
            temp = ListNode(result % 10)
            node.next = temp
            node = node.next
            l1 = l1.next

        while l2 is not None:
            result = l2.val + (1 if one else 0)
            one = result >= 10
            temp = ListNode(result % 10)
            node.next = temp
            node = node.next
            l2 = l2.next
        if one:
            node.next = ListNode(1)

        return ans.next
