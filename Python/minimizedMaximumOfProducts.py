class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # n stores
        # m products types, each of different amounts
        # m = len(quantities)
        # quantities[i] = quantity of ith product type.
        # every store can have at least 1 product and at max, max(quantities)
        # we simply have to iterate through in the range(1, max(quantities)), and for every j, :
        # the valid distributions for is sum of ceil(quantity[j]/i) for every j in quantities. 
        # check if total sum <= n and return accordingly

        def canDistributeValidly(k):
            totalStores = 0
            for quantity in quantities:
                totalStores += math.ceil(quantity/k)
            return totalStores <= n
        
        low, high = 1, max(quantities)
        while low < high:
            mid = (low + high) // 2
            if canDistributeValidly(mid):
                high = mid
            else:
                low = mid + 1
        return low
