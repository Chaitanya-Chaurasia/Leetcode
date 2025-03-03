class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        smaller, larger, pivots = [], [], []
        for i in nums:
            if i < pivot:
                smaller.append(i)
            elif i > pivot:
                larger.append(i)
            else:
                pivots.append(i)
        return smaller + pivots + larger
