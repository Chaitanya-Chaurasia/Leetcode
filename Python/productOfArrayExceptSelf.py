import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Define output result res, and two variables starting at length 1 and len(res) - 1.
        # Keep track of left and right products using 2 variables.
        # For every interation, update res[n] using left product, and res[k] with right product.
        # While n < k, do this. But as soon as n = k, res[n] is simply sum of left and right product.
        # After n and k cross each other, and n > k, res[n] is simply the product of res[n] and left product.
        # res[k] is simply the product of res[k] and right product.
        # This is because res[n] and res[k] have already been updated according to the opp. products.

        n = 1
        k = len(nums) - 2
        leftProduct = rightProduct = 1
        res = [1]* len(nums)

        while (n < len(nums)):

            leftProduct *= nums[n - 1]
            rightProduct *= nums[k + 1]

            if n < k:
                res[n] = leftProduct
                res[k] = rightProduct
            else:
                if n == k:
                    res[n] = leftProduct * rightProduct
                else:
                    res[n] *= leftProduct
                    res[k] *= rightProduct

            n += 1
            k -= 1

        return res
