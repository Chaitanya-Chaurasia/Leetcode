class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # since we can only delete one zero, unlike the previous question where we needed to find the maxConsecutive ones
        # we will introduce a new variable zeroes that will keep track of no of zeroes encountered.
        # we will move the window if no of zeroes exceeds 1

        zeroes, leftWindow, maxAns = 0, 0, 0

        for rightWindow in range(len(nums)):
            if nums[rightWindow] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[leftWindow] == 0:
                    zeroes -= 1
                leftWindow += 1
            
            # we also substract zeroes because there is a possiblity that at max, one zero can be deleted.
            # in case no of zeroes is 1, we will need to subtract that to get the max length
            maxAns = max(maxAns, rightWindow - leftWindow + 1 - zeroes)
        
        # in tc3, it says we must delete one element in case all elements are 1s
        if maxAns == len(nums):
            return maxAns - 1
        
        return maxAns       
