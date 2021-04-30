from log_variable import *

"""
is a function that takes another function as a parameter and extends its behaviour 
without modifying it.
"""


def my_decorator(target_function):
    def function_wrapper():
        return "Python is such a " + target_function() + " language!"

    return function_wrapper


@my_decorator
def target_function():
    return "cool"


log_variable("target_function()", target_function())
