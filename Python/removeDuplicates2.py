class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # our logic: same as removeDuplicates 1
        # since we need at max 2 repeating elements, we can simply start iterating from 2,
        # this is because we do not care about the the first two elements being either repeated or distinct
        # our append_pos will also be 2.
        # we need to compare element i with the element at append_pos - 2 and not i - 1.
        # this will guarantee that at max only two elements are added.
        if len(nums) <=2:
            return len(nums)

        append_pos = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[append_pos - 2]:
                nums[append_pos] = nums[i]
                append_pos += 1
        return append_pos
