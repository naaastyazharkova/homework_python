import string
import random

from random import choice



def create(k):
    r = ''
    for i in range(k):
        r += choice(string.ascii_letters)
    return r



print('Количество символов:')
r = int(input())
print(create(r))