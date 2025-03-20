# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # Our approach: One pass until both lists exist.
        # Make a new head, and keep appending digit sum to it. 
        # Trick is to include carry != 0 in while loop.

        carry = 0
        head = ListNode()
        temp = head

        while l1 or l2 or carry != 0:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0

            total = a + b + carry
            digitSum = total % 10
            carry = total // 10

            new = ListNode(digitSum)
            temp.next = new
            temp = temp.next
                
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        ans = head.next
        # head.next = None
        return ans
