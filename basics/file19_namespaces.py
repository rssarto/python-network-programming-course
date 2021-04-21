"""
Namespace - Space holding some names: Variables, Functions or Classes
types:
    The built-in namespace - contains python's built in functions
    The global namespace - contains variables or functions imported or created locally in or code
"""
# builtin functions
print(list(range(10)))

# the my_var was created in the global namespace
my_var = 10
print(my_var)

# variable defined in the global namespace
my_local_var = 20


def my_var_func():
    # local variable belonging to the my_var_func namespace
    my_local_var = 10
    print(my_local_var)


my_var_func()
print(my_local_var * 10)


def function_using_global_var():
    global my_local_var
    print(my_local_var)


function_using_global_var()
