class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # our logic -> iterate backwards and maintain three pointers
        # since both the lists are sorted ascending order, we can start by comparing the last elements of the list
        # if nums1[last] > nums2[last], append it to end, and update append_pos
        # if nums2[last] > nums1[last], it is the greatest element, and will append to back. then decrement pointers
        # we can continue this process until all elements in second element are not over.

        nums1_ptr, nums2_ptr, append_idx = m - 1, n - 1, m + n - 1
        while nums2_ptr >= 0:
            if nums1[nums1_ptr] > nums2[nums2_ptr] and nums1_ptr >= 0:
                nums1[append_idx] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[append_idx] = nums2[nums2_ptr]
                nums2_ptr -= 1
            append_idx -= 1
