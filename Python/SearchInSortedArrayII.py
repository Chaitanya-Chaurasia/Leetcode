class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        # Same as other variant, just a slight tweak
        # TRICK: Check if high, low and mid are all duplicates of each other

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[low] == nums[high]:
                low += 1
                high -= 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
