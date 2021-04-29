from log_variable import log_variable

a = lambda x, y: x * y
log_variable("type(a)", type(a))
log_variable("a(2, 10)", a(2, 10))
log_variable("a(5, 50)", a(5, 50))


def myfunc(mylist):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + mylist


log_variable("myfunc([100, 101, 102])", myfunc([100, 101, 102]))
b = lambda mylist: [x * y for x in range(10) for y in range(5)] + mylist
log_variable("b([100, 101, 102])", b([100, 101, 102]))

"""
map function
"""


# using a predefined function with map
def product10(a):
    return a * 10


range_seq = range(10)
log_variable("range(10)", range(10))
list_by_10_function = list(map(product10, range_seq))
log_variable("list_by_10_function", list_by_10_function)

# now using a lambda function with map
list_by_10_lambda = list(map((lambda a: a * 10), range_seq))
log_variable("list_by_10_lambda", list_by_10_lambda)

"""
filter function
"""
filter_result_list = list(filter((lambda a: a > 5), range_seq))
log_variable("filter_result_list", filter_result_list)
