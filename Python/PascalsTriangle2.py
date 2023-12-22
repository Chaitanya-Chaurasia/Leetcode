class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        triangle = [[1]]

        for i in range(rowIndex):
            
            previous = [0] + triangle[-1] + [0]
            new = []

            for j in range(len(previous) - 1):
                new.append(previous[j] + previous[j + 1])

            triangle.append(new)
            
        return triangle[-1]
        

        


      
