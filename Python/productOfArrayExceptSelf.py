# import numpy

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         self.newList = []
            
#         for i in range(0,len(nums)):
#             self.temp = []
#             self.temp.append(nums[0:i] + nums[i+1:len(nums)])
#             self.newList.append(numpy.prod(self.temp))

#             self.temp.clear()
        
#         return self.newList
            
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        products = [1] * length

        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]

        right = nums[-1]
        
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        
        return products
        
