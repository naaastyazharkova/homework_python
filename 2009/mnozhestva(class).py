set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
a = set_1.isdisjoint(set_2) 
b = set_1 == set_2
c = set_1.issubset(set_2)
d = set_1.issuperset(set_2)
e = set_1.union(set_2)
f = set_1.intersection(set_2)
g = set_1.difference(set_2)
h = set_1.symmetric_difference(set_2)
i = set_1.copy()
print(a, b, c, d, e, f, g, h, i)