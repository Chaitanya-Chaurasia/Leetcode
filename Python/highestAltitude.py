class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        net_altitude = 0
        maxAlt = 0

        for i in gain:
            net_altitude += i
            maxAlt = max(maxAlt, net_altitude)
        
        return maxAlt
