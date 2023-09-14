class Solution:
   def asteroidCollision(self, asteroids: List[int]) -> List[int]:
     
        stack = []
        
        for i in asteroids:
            while stack and (stack[-1] >=0 and i < 0) and  abs(stack[-1]) < abs(i) :
                stack.pop()
            
            if not(stack) or (stack[-1] < 0 and i >= 0) or (stack[-1] >=0 and i >= 0) or (stack[-1] <=0 and i <= 0) :
                stack.append(i)
            else: 
               
                if stack and abs(stack[-1]) == abs(i):
                    stack.pop()
                    
        return stack
