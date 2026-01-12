# Linear Time + Constant Space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1

        carry = 0
        prev = head = ListNode(0)
        while l1 or l2:
            value1, value2 = l1.val if l1 else 0, l2.val if l2 else 0
            nodeSum = value1 + value2 + carry
            if nodeSum > 9:
                carry, nodeSum = nodeSum // 10, nodeSum % 10
            else:
                carry = 0

            newNode = ListNode(nodeSum)
            prev.next = newNode
            prev = prev.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        prev.next = ListNode(carry) if carry == 1 else None

        return head.next
