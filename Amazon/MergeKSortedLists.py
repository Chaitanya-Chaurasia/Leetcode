# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Our Approach: Divide and Conquer
        # Split the lists into left and right recursively and merge them

        # Second Approach: Heap
        # Maintain a minHeap and add first node of k lists into the heap
        # Then, for every first node, if there is a next node, add that to heap.
        # 

        heap = []
        for i, head in enumerate(lists): 
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        head = ListNode(None)
        dummy = head

        while heap:
            val, i, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next

# class Solution:
#     # LeetCode 21. Merge Two Sorted Lists
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = prev = ListNode(0)
#         p1, p2 = list1, list2
#         while p1 and p2:
#             if p1.val < p2.val:
#                 prev.next = p1
#                 p1 = p1.next
#             else:
#                 prev.next = p2
#                 p2 = p2.next
#             prev = prev.next
#         prev.next = p1 if p1 else p2
#         return dummy.next
    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
        
#         while len(lists) > 1:
#             mergedLists = []
#             for i in range(0, len(lists), 2):
#                 list1 = lists[i]
#                 list2 = lists[i+1] if (i+1) < len(lists) else None
#                 mergedLists.append(self.mergeTwoLists(list1, list2))
#             lists = mergedLists
        
#         return lists[0]
