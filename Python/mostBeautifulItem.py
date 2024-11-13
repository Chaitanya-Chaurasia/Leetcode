class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        # def find_candidates(max_price):
        #     candidates = []
        #     for price, beauty in items:
        #         if price > max_price:
        #             break
        #         candidates.append([price, beauty])
        #     return candidates

        # def most_beautiful(candidates):
        #     max_beauty = 0
        #     for _, beauty in candidates:
        #         max_beauty = max(max_beauty, beauty)
        #     return max_beauty
        
        # result = []
        # for i in queries:
        #     items.sort(key=lambda x: x[0])
        #     candidates = find_candidates(i)
        #     result.append(most_beautiful(candidates))
        
        # return result

        # our approach: we preprocess and precalculate some parts.
        # we sort the list using the price as the key so we can group similar priced items and it is easier to search
        # then, we proceed by maintaining an array that stores the highest beauty value up until price "p". 
        # then, we iterate through queries and for each query, we iterate this precalculated array and get the result

        items.sort(key=lambda x:x[0])
        data, res = [[0, 0, float('inf')]], []

        # calculate max beauty b/w a range
        for price, beauty in items:
            prev_data = data[-1]
            if beauty >= prev_data[1]:
                prev_data[-1] = price 
                data.append([price, beauty, float('inf')])
        
        # since array is sorted, iterate backwards to find max beauty within a range and add it to res
        for upper_bound in queries:
            for idx in range(len(data) - 1, -1 , -1):
                if data[idx][0] <= upper_bound:
                    res.append(data[idx][1])
                    break
        return res
