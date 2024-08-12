class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if len(height) == 0:
            return 0

        i = 0
        j = len(height) - 1
        area = -1
        mh = max(height)

        while j != i:
            l = min(height[i], height[j])
            b = j - i 
            tempArea = l*b
            area = max(tempArea, area)

            # to reduce number of operations, check if max area has been reached. max area will be max(height)*width
            if area >= mh*b:
                break

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return area

            
        
