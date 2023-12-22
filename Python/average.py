class Solution:
    def average(self, sal: List[int]) -> float:
            min = max = sal[0]
            sum = 0
            for i in sal:
                if i < min:
                    min = i
                if i > max:
                    max = i
                sum += i
            return (sum - min - max) / (len(sal) - 2)
