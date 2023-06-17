"""
In the range 1 - 13 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13) the digit 1 occurs 6 times.

In the range, 1 - 2,660 (half the number of Romans in a legion),
expressed in Roman numerals, how many times does the numeral “X” occur?
"""


class Legionaries:

    def __init__(self, nRange):
        self.nRange = nRange
        self.keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        self.vals = ["I", "IV", "V", "IX", "X", "XL",
                     "L", "XC", "C", "CD", "D", "CM", "M"]
        self.roman = dict(zip(self.keys, self.vals))
        self.test()

    def toRoman(self, n):
        for i in self.keys[::-1]:
            x, y = divmod(n, i)
            yield self.roman[i] * x
            n -= i * x
            if n <= 0:
                break

    def legionaries(self) -> int:
        xNumerals: str = lambda n: "".join(list(self.toRoman(n)))
        xnums = list(map(xNumerals, list(self.nRange)))
        flt = filter(lambda n: "X" in n, xnums)
        numerals = list("".join(flt))
        return numerals.count("X")

    def test(self):
        print(self.legionaries())


nRange = range(1, 2661)
test = Legionaries(nRange)
