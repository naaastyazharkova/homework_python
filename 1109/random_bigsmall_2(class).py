import string
import random

from random import choice


def create(k):
    r = ''
    for i in range(k):
        r += choice(string.ascii_letters)
    return r


def count_str(s):
    big = 0
    small = 0
    for sym in s:
        if sym.isupper():
            big += 1
        else:
            small += 1
        if big > small:
            return 1
        elif small > big:
            return 0
        else: 
            return -1

print('Строка:')
n = int(input())
s = create(n)
print(s)
print(count_str(s))


