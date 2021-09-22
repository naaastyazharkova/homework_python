n = [1, 4, 4, 2, 7, 6, 6, 5, 0, 9]

def unique(n):
    list = []
    unique_n = set(n)

    for i in unique_n:
        list.append(i)
    
    return list

print (unique(n))