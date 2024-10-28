class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        # same approach as LCS. 
        # find n-1 and then start finding the sequence from there

        # nums = set(nums)
        # ans = -1
        # for i in nums:
        #     length = 0
        #     if math.sqrt(i) not in nums:
        #         length = 1 
        #         while i**2 in nums:
        #             length += 1
        #             i = i**2
        #         ans = max(ans, length) if length >= 2 else ans

        # return ans

        # better approach- using dp, but this will be o(nlogn)
        # approach, we sort the array. this way, we don't need to find n-1th element.
        # for every element, we maintain a hashset of count, and return the max count
        # if square is found, we add the count of square root and store it in the square's count
        # another observation, max length of subsequence can be 5 with given constraints
        nums = sorted(set(nums))
        dp = {i: 1 for i in nums}
        longest = 1
        for i in nums:
            nextElement = i**2
            if nextElement in dp:
                dp[nextElement] = dp[i] + 1
                longest = max(longest, dp[nextElement])
        return longest if longest >= 2 else -1        
