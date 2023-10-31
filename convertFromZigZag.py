class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows > len(s):
            return s

        # MAKE  2-D ARRAY
        rows = [[] for i in range(numRows)]

        # DEFINE VARS

        step = -1
        index = 0

        for i in s:

            rows[index].append(i)

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        # JOINING ALL ROWS TO ONE STRING -> GIVES 1D ARRAY
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        # CONVERTING 1D ARRAY TO STRING
        return ''.join(rows)
        
