class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        temp = nums

        if (temp.sort(reverse = True) == nums)

        while (l < r):
            if nums[r] > nums[l]:
                for i in range(r + 1, l):
                    if nums[l] < i < nums[r]:
                        return True
            else:
                l += 1
                r -= 1
        
        return False
    
