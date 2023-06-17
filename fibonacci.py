"""
The Fibonacci sequence begins like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
(each number is the sum of the previous two)

What is the sum of all odd numbers in the Fibonacci sequence that are less than 10,000?
"""


class Fibonacci:

    def __init__(self, n):
        self.n = n
        self.test()

    @staticmethod
    def fibonacci(x: int) -> int:
        """
        :return sum of odd Fibonacci numbers less than x
        """
        sumOdds, currFib = 1, 1
        i = 1
        while currFib < x:
            if currFib & 1:
                sumOdds += currFib
            # pow(x, n, m) := x**n % m
            currFib += pow(x, i, x * x - x - 1) // x
            i += 1
        return sumOdds

    def test(self) -> None:
        print(self.fibonacci(self.n))


_n = 10000
test = Fibonacci(_n)
