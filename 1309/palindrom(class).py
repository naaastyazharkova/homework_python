def get_format(s):
    return s == s[::-1]

b = input()
print(get_format(b)) 