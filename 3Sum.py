class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

    # WE NEED 3 POINTERS FOR THIS QUESTION

    # WE CAN HAVE THE TWO SUM LOGIC AND ADD ANOTHER LOOP TO ACCOUNT FOR 3rd ELEMENT

    # WE WILL NEED TO SORT THE ARRAY FIRST

    # THIS WAY, WE CAN ACCOUNT FOR DUPLICATES

        nums.sort()

        triplets = []

        for i in range(len(nums)):

            # CHECK FOR DUPLICATE FIRST ELEMENT
            # CONTINUE TILL THE DUPLICATE GROUP IS OVER

            if nums[i] == nums[i - 1] and i > 0:
                continue

            # NOW THAT I + 1th ELEMENT IS NOT DUPLICATE, WE PUT OUR TWOSUM LOGIC

            j = i + 1
            k = len(nums) - 1

            while j < k:

                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])

                if sum > 0: 
                    k -= 1
                
                else:
                    j += 1

                    # WE ALSO NEED TO CHECK FOR DUPLICATE J's. WE WILL USE ANOTHER WHILE LOOP TO GO TO THE END OF THE DUPLICATE STREAM "IF" THERE EXISTS ONE

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return triplets
        
