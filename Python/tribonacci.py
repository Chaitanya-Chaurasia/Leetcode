class Solution:
    def tribonacci(self, n: int) -> int:
        
        # bad space complexity
        # t = [0]*38
        # t[0], t[1], t[2] = 0, 1, 1

        # for i in range(3, n + 1):
        #     t[i] = t[i - 1] + t[i - 2] + t[i - 3]

        # use constant space
        x, y, z = 0, 1, 1

        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        
        res = 0
        for i in range(3, n + 1):
            res = x + y + z
            x = y
            y = z
            z = res
        
        return res

