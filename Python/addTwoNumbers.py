# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # APPROACH
        # Start with both the heads.
        # Check if both nodes exist, else assign 0 if either exists only.
        # Add the sum and make a new node, and assign to its value.
        # If sum in 2 digits, add appropriate carry over and go to next node.

        if not l1 and not l2:
            return None 

        carry = 0
        dummy = ListNode(0)
        tail = dummy

        while l1 or l2 or carry != 0:
            
            s = 0
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            s = a + b + carry

            # Get the last digit
            digit = s % 10

            # Get the first digit
            carry = s // 10

            newHead = ListNode(digit)
            tail.next = newHead
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummy.next
        dummy.next = None
        return result
