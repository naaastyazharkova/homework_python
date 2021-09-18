def get_extension(string:str):
    return string.split('.')[1]

print('Введите файл:')
a = input()
print(get_extension(a))



