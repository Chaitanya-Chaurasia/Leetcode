class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        # Trick: Simple DA + Prefix Sum
        
        k, prefix = len(bookings), 0
        diff = [0] * (n + 2)
        res = [0] * (n + 1)

        for f, l, seats in bookings:
            diff[f] += seats
            diff[l + 1] -= seats

        for i in range(1, n + 1):
            prefix += diff[i]
            res[i] = prefix
        
        return res[1:]
