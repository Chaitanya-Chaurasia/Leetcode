class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        # TWO POINTER SOLUTION GREEDY METHOD

        l = 0
        r = len(height) - 1

        # STORE MAX_AREA IN MOST
        most = 0

        # WE WILL FIND THE AREA OF CONTAINERS UNTIL THE TWO POINTERS COINCIDE
        # FIND THE AREA, AND UPDATE MOST
        # IF RIGHT HEIGHT IS MORE, INCREMENT LEFT POINTER AS GREATER HEIGHT CAN COMPENSATE FOR SMALLER WIDTH
        # ELSE DECREMENT RIGHT POINTER

        while l < r:

            print(f"Container dimensions : {height[l]} {height[r]}")

            h = min(height[r], height[l])
            width = r - l
            area = h * width
            most = max(area, most)

            if height[r] > height[l]:
                l += 1
            else: 
                r -= 1

        return most
