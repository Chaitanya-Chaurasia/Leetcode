class Solution:
    def trap(self, height: List[int]) -> int:

        # Our Approach: 2 Pointer Solution
        # Keep track of left and right max-heights.
        # In every iteration, we calculate the amount of water using left/right ptr - height[i]
        # Then, we update the left/right ptr in case height[i] > ptr.

        left, right, leftMax, rightMax, water = 0, len(height) - 1, height[0], height[-1], 0

        while left < right:
            if leftMax <= rightMax:
                water += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])

            else:
                water += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])

        return water

        # Approach 2: DP
        # Compute leftMax and rightMax arrays
        # Then, at every index, find the amount of water trapped
        # l = len(height)
        # leftMax, rightMax,  = [0] * l, [0] * l
        # leftMax[0] = height[0]
        # rightMax[-1] = height[-1]


        # for i in range(l):
        #     leftMax[i] = max(height[i], leftMax[i - 1])

        # for i in range(l - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])        

        # water = 0
        # for i in range(l):
        #     water += min(leftMax[i], rightMax[i]) - height[i]
        
        # return water
