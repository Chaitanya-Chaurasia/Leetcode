# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None
        
        first_ptr, second_ptr = head, head.next.next
        
        while second_ptr and second_ptr.next:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next.next        
      
        first_ptr.next = first_ptr.next.next

        return head      
