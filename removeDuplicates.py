# Leetcode Problem 26

# Intuition

# Start iterating from index 1
# if nums[i] != nums[i-1], index has changed. Update value at j, and return j

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) != 0 or len(nums) != 1:
            j = 0
            l = len(nums)

            for i in range(1, l) :

                if nums[i] != nums[i - 1]:
                    j += 1
                    nums[j] = nums[i]
            
            return j + 1
        
        return len(nums)
