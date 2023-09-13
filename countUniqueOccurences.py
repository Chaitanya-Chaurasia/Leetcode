class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # Slow approach
        # if len(arr) == 1:
        #     return True
        # hashSet = {}
        # count = []

        # for i in arr:
        #     if i in hashSet:
        #         hashSet[i] += 1
        #     else:
        #         hashSet[i] = 0
        
        # for i in hashSet:
        #     count.append(hashSet[i])

        # count.sort()

        # for i in range(1, len(count)):
        #     if count[i] == count[i - 1]:
        #         return False

        # return True

        # Faster
        if len(arr) == 1:
            return True
        
        count = []
        occured = []

        for i in arr:
            if i in occured:
               continue
            else:
                if arr.count(i) not in count:
                    count.append(arr.count(i))
                    occured.append(i)
                else:
                    return False

        return True
        

        
