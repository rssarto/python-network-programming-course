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
