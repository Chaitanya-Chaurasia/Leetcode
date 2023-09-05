class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

       
        lsum = 0
        rsum = sum(nums)

        for index, element in enumerate(nums):
            rsum -= element

            if lsum == rsum:
                return index
            
            lsum += element

        return -1
            
