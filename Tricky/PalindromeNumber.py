class Solution:
    def isPalindrome(self, x: int) -> bool:

        # DO NOT TAKE THE CONVERTING TO STRING APPROACH
        # USE MATH
        # Approach: Use remainder and integer division

        # Two things to remember, for any number, we can get the last digit from x % 10. (remainder)
        # To remove a digit from a number, we simply do x // 10. For ex, 145 becomes 140/.  
        # In this problem, we keep on doing the same. until our number doesn't get 0.
        # We will multiply each digit we get with 10 and add remainder.

        if x < 0:
            return False
        
        reverse = 0
        temp = x

        while temp > 0:
            
            # Get last digit
            lastDigit = temp % 10

            reverse = (reverse * 10) + lastDigit
            
            # Remove a digit
            temp = temp // 10

        return x == reverse        
