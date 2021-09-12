import string

s= string.ascii_lowercase
l = list(s)

def p_while(l):
	i=0
	while i < len(l):
		print (l)
		i+=1
	return l

print(p_while(l))

