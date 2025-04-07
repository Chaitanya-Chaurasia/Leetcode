# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Our approach: Reverse from Midpoint and Merge
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now, we're at midpoint
        mid = slow
        prev, cur = None, mid

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        first, second = head, prev

        # Now, we need a reference to first and second both, so we can refer to their next pointers.
        # We use a variable temp for it.
        # Initially, we assign first.next = second, and store the original "first" in temp, 
        # This is so we can get first.next.
        # Next, we do the same with second.

        while second.next:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
