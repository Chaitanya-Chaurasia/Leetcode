

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        self.temp = []
        self.new = []

        for i in range(0, len(nums)):
            self.temp.append(nums[i])
            nums = nums[0:i] + nums[i+1:]
            self.new.append(math.prod(nums))
            nums.insert(i, self.temp[0])
            del self.temp[0]

        return self.new
            

        
