# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # make 2 pointers at index 0 and 1.
        # delete all even positions at first pointer and add all even positions on second ptr.
        # odd.next = even

        if not head.next or not head:
            return None

        odd = head
        even = head.next
        odd_to_even = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = odd_to_even
        return head
        
