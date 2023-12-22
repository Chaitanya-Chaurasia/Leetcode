class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def BinarySearch(i, j): 
            
            mid = (i + j)// 2

            if nums[mid] == target:
                return mid
            
            if target > nums[mid] and target <= nums[mid+1]:
                return mid+1
            
            if nums[mid] > target:
                return BinarySearch(i, mid)
            else:
                return BinarySearch(mid, j)

        if target > nums[-1]:
            return len(nums)
        
        if target < nums[0]:
            return 0

        return BinarySearch(0, len(nums) - 1)

        

