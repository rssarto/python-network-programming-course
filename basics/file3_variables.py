my_var = 10
print(str.format('my_var = {}', my_var))

a = b = c = 10
print(str.format('a = {}, b = {} and c = {}', a, b, c))

d, e, f = 11, 12, 13
print(str.format('d = {}, e = {} and f = {}', d, e, f))

# Address or identity of a variable in memory
print(str.format('my_var memory address: {}', id(my_var)))
print(str.format('memory address of 10: {}', id(10)))
my_other_var = my_var
print(str.format('my_other_var memory address: {}', id(my_other_var)))
my_other_var = 20
print(str.format('my_other_var memory address: {}', id(my_other_var)))
