class Solution:
    def fib(self, n: int) -> int:

        first = 0
        second = 1
        
        if n == 0:
            return first

        if n == 1:
            return first + second

        fib = 1

        for i in range(2, n + 1):
            fib = first + second
            first = second
            second = fib
        
        return fib
