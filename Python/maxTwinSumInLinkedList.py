# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # use slow and fast pointers to find midpoint.
        # then reverse the second half of the list
        # now, use 2 pointer method to calculate max sum

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        max_sum = 0
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head, prev = head.next, prev.next
        
        return max_sum
