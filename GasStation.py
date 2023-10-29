class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # If cost of gas required is greater than the gas available, return
        if sum(cost) > sum(gas):
            return -1
        
        # Intially, gas remaining is 0, as we do not have gas filled
        gas_remaining = 0

        # station is also 0
        station  = 0
        
        for i in range(len(gas)):
            
            # Calculate gas for every station
            gas_remaining += gas[i] - cost[i]

            # if gas is negative, increment station, denoting the next gas station is where
            # the driver could start from

            # Our gas_remaining will again become 0

            if gas_remaining < 0:
                station = i + 1
                gas_remaining = 0

        return station

        






