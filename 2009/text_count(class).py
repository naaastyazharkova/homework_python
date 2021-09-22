import string
from typing import Text
def count_letters(text):
    d = {}
    for i in string.ascii_letters:
        d[i] = text.count(i)
    return d
a = string.ascii_letters
print(count_letters(a))