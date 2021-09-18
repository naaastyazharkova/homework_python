def n_of_n(n):
	list_ = []
	list_.append(int(str(n)*2))
	list_.append(int(str(n)*3))
	list_.append(n)
	return sum (list_)

a = int(input())
print(n_of_n(a))




