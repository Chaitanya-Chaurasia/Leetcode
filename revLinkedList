# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    # |   |   |
    #     1->2->3->4->None

        curr = head
        prev = None

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


        
