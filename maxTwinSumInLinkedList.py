# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:


        prev = None
        nex = None
        slow = head
        fast = head
        maxSum = 0

        while fast and fast.next:
            fast = fast.next.next
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex

        while slow and prev:
            if maxSum == None or slow.val + prev.val > maxSum:
                maxSum = max(slow.val + prev.val, maxSum)

            slow = slow.next
            prev = prev.next
        
        return maxSum



        
