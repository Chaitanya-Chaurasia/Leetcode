class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # Iterate through the asteroids list, and append to stack such that it is stable
        # Check for collision on adding a new element, if yes, backtrace the stack and keep popping until it stops.
        # If not, keep on adding to stack to keep it stable.

        stack = []

        for i in asteroids:
            
            # if stack[-1] is positive and asteroid is negative, keep popping
            while stack and (stack[-1] >= 0 and i < 0) and (abs(i) > stack[-1]):
                stack.pop()
            
            # if both asteroids are same directions, or if opposite direction (for eg: [....., -10] and 10)
            if not stack or (stack[-1] < 0 and i <= 0) or (stack[-1] > 0 and i>= 0) or (stack[-1] < 0 and i >=0):
                stack.append(i)

            # if both are of equal magnitude and heading towards each other.
            elif stack[-1] and stack[-1] + i == 0:
                stack.pop()
                
        return stack
