class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxVolume = 0
        l = 0
        r = len(height) - 1

        while (l < r):

            maxV = (r - l)*min(height[l],height[r])
            maxVolume = max(maxV, maxVolume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxVolume
        
        
