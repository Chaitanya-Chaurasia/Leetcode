import heapq

class Solution:
    def topKFrequent(self, num: List[int], k: int) -> List[int]:

        # METHOD 1- MAX HEAP 0(klogn)

        counter = Counter(num)
        heap = []

        for value, freq in counter.items():
            heapq.heappush(heap, (-freq, value)) 

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result


        # METHOD 2- BUCKET SORT 0(n)

        d = {}

        # COUNT STARTS FROM 1 TO LEN(NUMS). COUNT CANNOT BE 0
        count = [[] for _ in range(len(num) + 1)]

        # COUNT FREQUENCY OF EACH ELEMENT
        for i in num:
            d[i] = 1 + d.get(i, 0)

        # STORE COUNT, [ELEMENT] IN THE NEW ARRAY

        for element, freq in d.items():
            count[freq].append(element)

        # NOW START FROM BACK, SINCE COUNT IS SORTED, AND KEEP ON ADDING TO A RESULT ARRAY,
        # UNTIL LENGTH OF RESULT IS K
        
        result = []

        for i in range(len(count) - 1, 0, -1):
            for element in count[i]:
                result.append(element)
                if len(result) == k:
                    return result

        return num
        



        
