class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        # calculate the count of each element in a hashmap
        # then iterate over the array, and check if count is 1, reduce k by 1

        hashmap = {}

        for i in arr:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in arr:
            if hashmap[i] == 1:
                k -= 1
            
            if k == 0:
                return i
        
        return ""
