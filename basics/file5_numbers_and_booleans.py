from file4_strings import log_variable

# Integers and float pointing numbers
log_variable("type(10)", type(10))
log_variable("type(2.5)", type(2.5))

# mathematical operations
log_variable("1 + 2", 1 + 2)
log_variable("10 + 2.5", 10 + 2.5)
log_variable("2 - 1", 2 - 1)
log_variable("5 / 2", 5 / 2)
log_variable("5 // 2", 5 // 2)
log_variable("4 * 2", 4 * 2)
log_variable("4 ** 2", 4 ** 2)
log_variable("5 % 2", 5 % 2)

# number comparisons
log_variable("4 < 5", 4 < 5)
log_variable("5 > 4", 5 > 4)
log_variable("4 <= 5", 4 <= 5)
log_variable("5 >= 4", 5 >= 4)
log_variable("5 == 5", 5 == 5)
log_variable("4 != 5", 4 != 5)

# operations precedence: 1 raising to a power / 2 multiplication, division, modulo / 3 addition, subtraction
log_variable("100 - 5 ** 2 / 5 * 2", 100 - 5 ** 2 / 5 * 2)

# convert float to int
log_variable("int(1.7)", int(1.7))

# convert int to float
log_variable("float(2)", float(2))

# absolute value
log_variable("abs(5)", abs(5))
log_variable("abs(-5)", abs(-5))

# min and max from set of numbers
log_variable("max(1, 2)", max(1, 2))
log_variable("max(1, 2, 0)", max(1, 2, 0))
log_variable("min(1, 2)", min(1, 2))
log_variable("min(1, 2, 0)", min(1, 2, 0))

# power function instead of ** operator
log_variable("pow(3, 2)", pow(3, 2))

# booleans: True / False
log_variable("1 == 1", 1 == 1)
log_variable("1 == 2", 1 == 2)
log_variable("\"python\" == \"python\"", "python" == "python")
log_variable("\"python\" == \"Python\"", "python" == "Python")
log_variable("3 <= 4", 3 <= 4)

# boolean operators: and, or and not
log_variable("(1 == 1) and (2 == 2)", (1 == 1) and (2 == 2))
log_variable("(1 == 2) and (3 == 2)", (1 == 2) and (3 == 2))
log_variable("(1 == 1) and (3 == 2)", (1 == 1) and (3 == 2))
log_variable("(1 == 1) or (2 == 2)", (1 == 1) or (2 == 2))
log_variable("(1 == 1) or (3 == 2)", (1 == 1) or (3 == 2))
log_variable("(1 == 2) or (3 == 2)", (1 == 2) or (3 == 2))
log_variable("not(1 == 1)", not(1 == 1))
log_variable("not(1 == 2)", not(1 == 2))

# values that always evaluate to False: None, 0, 0.0, 0j, "", [], (), {}
# values that evaluate fo True: 1, 2.5, "hello"
log_variable("bool(None)", bool(None))
log_variable("bool(0)", bool(0))
log_variable("bool(0.0)", bool(0.0))
log_variable("bool(0j)", bool(0j))
log_variable("bool("")", bool(""))
log_variable("bool([])", bool([]))
log_variable("bool(1)", bool(1))
log_variable("bool([1])", bool([1]))
log_variable("bool(\"router\")", bool("router"))
