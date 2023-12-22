class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        triangle = [[1]]

        for i in range(numRows - 1):
            
            previous = [0] + triangle[-1] + [0]
            new = []

            for j in range(len(previous) - 1):
                new.append(previous[j] + previous[j + 1])

            triangle.append(new)
            
        return triangle
        

        

