"""
Epigram on Failure

Considering only the alphabetical characters, consonants having the value of their ASCII codes,
and vowels having the inverse value of their ASCII codes, what is the sum of the sentence?

Example: Taking the word “iffy”, the ASCII code of “i” is 105, it’s inverse is -105. The ASCII 
value of ‘f’ is 102. The ASCII y of “y” is 121. The sum of “iffy” = 220
"""


class SentenceSum:

    def __init__(self, string):
        self.string = string
        self.test()

    def sentenceSum(self) -> int:
        flt = filter(str.isalpha, self.string)
        string = "".join(flt).lower()
        getCode: int = lambda c: -ord(c) if c in 'aeiou' else ord(c)
        return sum(map(getCode, string))

    def test(self) -> None:
        print(self.sentenceSum())



str1 = "iffy"
str2 = "automatically"
str3 = "user 5 contributions % licensed under *"
test1 = SentenceSum(str1)  # 220
test2 = SentenceSum(str2)  # 153
test3 = SentenceSum(str3)  # 671
