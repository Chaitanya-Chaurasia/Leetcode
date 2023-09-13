class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        if len(arr) == 1:
            return True
        hashSet = {}
        count = []

        for i in arr:
            if i in hashSet:
                hashSet[i] += 1
            else:
                hashSet[i] = 0
        
        for i in hashSet:
            count.append(hashSet[i])

        count.sort()

        for i in range(1, len(count)):
            if count[i] == count[i - 1]:
                return False

        return True
        
