def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(35, 'Zenit', False)
print_params(21, 'домашний')
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [32, 'CSKA', 23.3]
values_dict = {'a': 23, 'b': 'PRIMER', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [24.3, 'World']
print_params(*values_list_2, 42)