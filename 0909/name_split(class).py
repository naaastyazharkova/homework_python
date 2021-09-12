name = 'Zharkova Anastasia Andreevna'

def initials(name):
    start = 0
    result= name.split()
    return result[0] + ' ' + result[1][0:1] + '. ' + result[2][0:1] + '. ' 

print(initials(name))
