from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        # our approach is simple
        # since we need to check for subarray of size k that is both consecutive and sorted, we can use sliding window.
        # we can maintain count of consecutive elements in a window, and update it depending on new additions and deletions to window

        left, res, power = 0, [], 1
        for right in range(len(nums)):

            # condition to increment right pointer
            if right > 0 and nums[right - 1]  + 1 == nums[right]:
                power += 1
            
            # condition to increment left pointer i.e when size of window is > k
            # windowSize = right - left + 1
            if right - left + 1 > k:
                if nums[left + 1] == nums[left] + 1:
                    power += 1
                left += 1
            
            # append max to subarray
            if right - left + 1 == k:
                res.append(nums[right] if power == k else -1)
        return res
