def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#  Первый пункт задачи
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print()

#  Второй пункт задачи
values_list = ["First", False, 8]
values_dict = {"a": "Second", "b": True, "c": 9}
print_params(*values_list)
print_params(**values_dict)
print()

#  Третий пункт задачи
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
