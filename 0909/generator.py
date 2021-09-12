names  = ['Zharkova Anastasia Andreevna', 'Zharkov Nikita Andreevich', 'Baranova Arina Pavlovna', 'Kartashov Artem Yurievich']

from random import randrange

def gen(n):
    i = 0
    while i < n:
        s = ''
        for k in range(0, 3):
            s += chr(randrange(68, 90))
            s += chr(randrange(97, 118)) * 3
            if k < 3:
                s += ' '
        yield s
        i += 1

def initials(name):
    l = name.split()
    return l[0] + ' ' + l[1][0:1] + '. ' + l[2][0:1] + '.' 

def initials_more(names):
    result = []
    for name in gen(10):
        new_name = initials(name)
        result.append(new_name)

    return result

print(initials_more(names))




