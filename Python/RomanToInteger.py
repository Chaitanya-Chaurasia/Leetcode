class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
       
        # TIP: Start from the front of the string and go replacing characters from the map. 
        # If s[i + 1] > s[i] i.e an instance such as IV or XL, we simply subtract s[i] from the result.
        # At the same time, we need to append hashmap[s[i]] to our total
        # You will notice that this method will only go on until len(s) - 1 because of our condition.
        # This is why we append s[-1] to the result at the end. 
        num = 0
        for i in range(len(s) - 1):
            if hashmap[s[i + 1]] > hashmap[s[i]]:
                num -= hashmap[s[i]]
            else:
                num += hashmap[s[i]]
        return num + hashmap[s[-1]]
