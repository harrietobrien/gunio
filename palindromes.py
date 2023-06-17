"""
A palindrome is a word, number, phrase, or another sequence of characters which
reads the same backward as forward, such as madam, racecar, or the number 10801

What is the sum of all numeric palindromes that are less than 10,000?
"""


class Palindrome:

    def __init__(self, n):
        self.n = n
        self.test()

    @staticmethod
    def isPalindrome(x: int) -> bool:
        digits = list()
        tmp = x
        count = 0
        while tmp > 0:
            digits.append(tmp % 10)
            tmp //= 10
            count += 1
        i, k = 0, len(digits)
        rev = 0
        while k > 0:
            rev += digits[i] * 10 ** (k - 1)
            i += 1
            k -= 1
        return x == rev

    def palindromeSum(self) -> int:
        return sum(filter(lambda n: self.isPalindrome(n),
                          list(range(1, 10000))))

    def test(self):
        print(self.palindromeSum())


_n = 10000
test = Palindrome(_n)
