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

        if head == None or head.next == None: 
            return head

        odd = head
        even = head.next
        odd_to_even = even

        while even != None and even.next != None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = odd_to_even
        return head
        
