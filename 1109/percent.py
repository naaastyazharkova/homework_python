from array import array
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
    for x in s:
        if x.isupper():
            big += 1
        else:
            small += 1
        if big > small:
            return 1
        elif small > big:
            return 0
        else: 
            return -1

def per(array):
    big_let = 0
    small_let = 0
    same = 0
    for x in array:
        if count_str(x) == 1:
            big_let += 1
        elif count_str(x) == 0:
            small_let += 1
        else:
            same += 1
    per_big = (big_let / len(array)) * 100
    per_small = (small_let / len(array)) * 100
    per_same = (same / len(array)) * 100
    s = f'В строке {round(per_big)}% заглавных букв, {round(per_small)}% строчных букв, {round(per_same)}% - букв поровну' 
    return s

print(per(create(3)))