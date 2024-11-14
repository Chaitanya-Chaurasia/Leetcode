class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # since we are not given k, the maximum value of k can be the max value of piles.
        # koko can at least eat 1 banana in h hours and at max, max(piles) banana.
        # to find the most suitable, instead of linear search and calculation, we make use of binary search
        # linear search is brute force, binary search is optimized
        # for every possible "k", we need to check if all bananas can be finished in h hours.
        
        def canEatAllBananas(k):
            hours = 0
            for bananas in piles:
                # we use ceil because we need to round UP to the closest integer
                # it is the same as pile + k - 1 // k
                hours += math.ceil(bananas/k)
            return hours <= h

        # BRUTE FORCE APPROACH (GIVES TLE)
        # minimum_time = float('inf')
        # for i in range(1, max(piles)):
        #     res = canEatAllBananas(i)
        #     if res:
        #         minimum_time = min(minimum_time, i)
        #     else:
        #         minimum_time = max(piles)
        # return minimum_time

        low, high = 1, max(piles)
        while low < high:
            mid = (low + high)//2
            if canEatAllBananas(mid):
                high = mid
            else:
                low = mid + 1

        # we return low because we need the least possible value
        # if we wanted to calculate the maximum possible value, return high
        return low
