class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # brute force (not in-place) BAD Solution
        # uniques = []
        # for i in nums:
        #     if i not in uniques:
        #         uniques.append(i)
        # print(uniques)
        # for i in range(len(uniques)):
        #     nums[i] = uniques[i]
        
        # return len(uniques)

        # our approach, start iterating at 1, and look at previous element.
        # if same, continue
        # if different, update pointers, and insert at append_pos. update the append_pos

        if len(nums) == 1:
            return 1
        
        append_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[append_pos] = nums[i]
                append_pos += 1
        return append_pos
