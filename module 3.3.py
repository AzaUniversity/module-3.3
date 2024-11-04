def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = 5, 'banana', [2,3,4,5]
values_dict = {'a' : 4, 'b' : 'Evgeniy' , 'c' : 555}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = 44, 'need'
print_params(*values_list_2, 42)