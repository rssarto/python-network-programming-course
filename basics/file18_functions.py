from log_variable import log_variable

"""
Code isolated in block that can be reused
"""


def my_first_function():
    "This is our first function!"
    print("Hello Python!")


my_first_function()
help(my_first_function)


def my_second_function(x):  # parameter
    print(x)


my_second_function("Ricardo")  # argument


def my_third_function(x, y):
    print("Hello " + x)
    print("Hello " + y)


my_third_function("Python", "Java")


def my_sum(x, y):
    sum = x + y
    return sum


log_variable("my_sum(1, 2)", my_sum(1, 2))


def my_second_sum(x, y, z):
    sum = (x + y) * z
    return sum ** 2


log_variable("my_second_sum(1, 2, 3)", my_second_sum(1, 2, 3))  # positional arguments

# keyword arguments
log_variable("my_second_sum(x=1, y=2, z=3)", my_second_sum(x=1, y=2, z=3))
log_variable("my_second_sum(z=3, x=1, y=2)", my_second_sum(z=3, x=1, y=2))

# not allowed usage of keyword arguments
# my_second_sum(x=1, y=2, 3)

# allowed usage of positional and keyword arguments
log_variable("my_second_sum(1, 2, z=3)", my_second_sum(1, 2, z=3))
log_variable("my_second_sum(10, 12, z=3)", my_second_sum(10, 12, z=3))
log_variable("my_second_sum(110, 120, z=3)", my_second_sum(110, 120, z=3))


# default parameter value
def my_third_sum(x, y, z=3):
    sum_xyz = (x + y) * z
    return sum_xyz


log_variable("my_third_sum(1, 2)", my_third_sum(1, 2))
log_variable("my_third_sum(1, 2, 4)", my_third_sum(1, 2, 4))


# variable number of positional parameters
def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)


function1("Hello")
function1("Hello", 100, 200)


# variable number of keyword arguments
def function2(x, **kwargs):
    print(x)
    for item in kwargs.items():
        print(f"{item.__getitem__(0)} = {item.__getitem__(1)}")


function2(2, k=2, j=3, y=10)
