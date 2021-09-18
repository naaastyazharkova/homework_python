import string
s= string.ascii_lowercase
l3 = list(s)

def show(func):
    def n_func(*args, **kwargs):
        result = 0
        print('Function - ', func.__name__)
        print('Positional arguments are:', args)
        print('Keyword arguments are:', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return n_func

@show

def p_for(l3):
	for el in l3:
            print(el)

show(p_for(l3))
p_for(4, 8)

print (p_for(l3))