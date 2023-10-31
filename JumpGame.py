class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # GREEDY 1
        # # MAX JUMP POSSIBLE
        # jump = 0

        # for i in range(len(nums)):

        #     # IF INDEX IS NOT REACHABLE, EXIT
        #     if i > jump:
        #         return False

        #     # INCREMENT JUMP BY MAX VALUE OF CURRENT JUMP AND i + nums[i] (WE COULD JUST DO +=,BUT WE CONSIDER THE CASE OF 0 AS WELL)
        #     jump = max(jump, i + nums[i])

        # return True

        # GREEDY 2

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
