from log_variable import log_variable

"""
iter function
"""
my_list = [1, 2, 3, 4, 5, 6, 7]

# using a regular for to iterate the list
for element in my_list:
    log_variable("element", element)

# using an iterator to iterate the list
my_list_iterator = iter(my_list)
log_variable("type(my_list_iterator)", type(my_list_iterator))
log_variable("next(my_list_iterator)", next(my_list_iterator))

"""
generators
"""


def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y


my_object = my_gen(10, 5)
log_variable("type(my_object)", type(my_object))
log_variable("next(my_object)", next(my_object))
while (1):
    value = next(my_object, 'end')
    if value == 'end':
        break
    else:
        log_variable("value", value)

"""
generator expressions
"""
gen_exp = (x for x in range(5))
log_variable("type(gen_exp)", type(gen_exp))
while(1):
    value = next(gen_exp, "end")
    if value == "end":
        break
    log_variable("value", value)
