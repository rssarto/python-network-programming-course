from log_variable import log_variable

"""
if <expression>:
    ...
elif <expression>:
    ...
else:
    ...
"""
x = 10
if x > 5:
    log_variable("if x > 5", x > 5)
    log_variable("x * 2", x * 2)

x = 4
if x > 5:
    log_variable("if x > 5", x > 5)
    log_variable("x * 2", x * 2)
else:
    log_variable("if x > 5", x > 5)

x = 5
if x > 5:
    log_variable("if x > 5", x > 5)
    log_variable("x * 2", x * 2)
elif x == 5:
    log_variable("if x == 5", x == 5)
else:
    log_variable("if x > 5", x > 5)

if x == 5 and type(x) is int:
    log_variable("x == 5 and type(x) is int", x == 5 and type(x) is int)
elif x == 10 and type(x) is int:
    log_variable("x == 10 and type(x) is int", x == 10 and type(x) is int)

x = 10
if x == 5 and type(x) is int:
    log_variable("x == 5 and type(x) is int", x == 5 and type(x) is int)
elif x == 10 and type(x) is int:
    log_variable("x == 10 and type(x) is int", x == 10 and type(x) is int)

x = 100
if x == 5 and type(x) is int:
    log_variable("x == 5 and type(x) is int", x == 5 and type(x) is int)
elif x == 10 and type(x) is int:
    log_variable("x == 10 and type(x) is int", x == 10 and type(x) is int)
