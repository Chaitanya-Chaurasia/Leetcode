class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        max_heap = [(-freq, ch) for ch, freq in hashmap.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap) >= 2:
            
            f1, c1 = heapq.heappop(max_heap)
            f2, c2 = heapq.heappop(max_heap)

            res.extend([c1, c2])

            if f1 + 1 < 0:
                heapq.heappush(max_heap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(max_heap, (f2 + 1, c2))
        
        if max_heap:
            f, c = heapq.heappop(max_heap)
            if -f > 1:
                return ""
            res.append(c)
        return "".join(res)
