# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head == None or head.next == None:
            return None

        # give the fast pointer a gap of n nodes
        # iterate both slow and fast by one step.
        # when fast reaches null, we are at the nth node from end

        prev = ListNode(0, head)
        fast, slow = prev, prev

        for _ in range(n + 1):
            fast = fast.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return prev.next
