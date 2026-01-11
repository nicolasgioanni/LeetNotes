# Polynomial Time (n * m) + Constant Space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        start = 0
        while not lists[start]:
            start += 1
        result = lists[start]

        for i in range(start + 1, len(lists)):
            l1, l2 = result, lists[i]

            if l1.val > l2.val:
                head = curr = l2
                l2 = l2.next
            else:
                head = curr = l1
                l1 = l1.next

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            result = head
        return head
