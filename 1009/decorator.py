import string
s= string.ascii_lowercase
l3 = list(s)

def show(func):
    def n_func(*args, **kwargs):
        result = 0
        print('Function - ', show(func))
        print('Positional arguments are:', args)
        print('Keyword arguments are:', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return n_func

def p_for(l3):
	for el in l3:
            print(el)

watch = show(p_for(l3))
watch(1,3)

@show

def p_for(l3):
	for el in l3:
            print(el)

p_for(1, 3)

print (p_for(l3))