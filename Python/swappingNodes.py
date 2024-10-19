# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # iterate to kth element from front
        # iterate to kth element from back
        # swap values

        if head is None:
            return None

        if head.next is None and k == 1:
            return head

        first = head
        pos = 0
        while pos != k - 1:
            first = first.next
            pos += 1

        slow, fast = head, head

        for _ in range(k):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        first.val, slow.val = slow.val, first.val

        return head
