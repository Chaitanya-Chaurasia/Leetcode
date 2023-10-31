class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # MAKE WINDOWS TO DENOTE THE AVAILABLE SPACE INDEX i CAN JUMP TO
        # KEEP ON MAKING SUCH WINDOWS BY INCREMENT L = R + 1 AND R = MAX(WINDOW)

        l = 0
        r = 0
        count = 0

        while r < len(nums) - 1:

            new_r = 0

            # FIND MAX(WINDOW)
            for i in range(l, r + 1):
                new_r = max(new_r, i + nums[i])

            # SHIFT WINDOW
            l = r + 1
            r = new_r

            # INCREMENT COUNT
            count += 1

        return count



