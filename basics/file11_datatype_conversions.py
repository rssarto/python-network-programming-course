from log_variable import log_variable

log_variable("type(2)", type(2))
log_variable("type(2.5)", type(2.5))

# Converting from int to string
log_variable("str(2)", str(2))
log_variable("type(str(2))", type(str(2)))

# Converting from floating point to string
log_variable("str(2.5)", str(2.5))
log_variable("type(str(2.5))", type(str(2.5)))

# Converting from int to string
log_variable("str(\"5\")", str("5"))
log_variable("type(str(\"5\"))", type(str("5")))
log_variable("int(\"5\")", int("5"))
log_variable("type(int(\"5\"))", type(int("5")))

# Converting from floating point to string
log_variable("float(\"5.2\")", float("5.2"))
log_variable("type(float(\"5.2\"))", type(float("5.2")))

# Converting int to floating points
log_variable("type(2)", type(2))
log_variable("float(2)", float(2))
log_variable("type(float(2))", type(float(2)))

# Converting floating points to int
log_variable("type(12.4)", type(12.4))
log_variable("int(12.4)", int(12.4))
log_variable("type(int(12.4))", type(int(12.4)))

log_variable("type(12.7)", type(12.7))
log_variable("int(12.7)", int(12.7))
log_variable("type(int(12.7))", type(int(12.7)))

# Converting tuple to list
log_variable("type((1, 2, 3))", type((1, 2, 3)))
log_variable("list((1, 2, 3))", list((1, 2, 3)))
log_variable("type(list((1, 2, 3)))", type(list((1, 2, 3))))

# Converting a list to tuple
log_variable("type([1, 2, 3])", type([1, 2, 3]))
log_variable("tuple([1, 2, 3])", tuple([1, 2, 3]))
log_variable("type(tuple([1, 2, 3]))", type(tuple([1, 2, 3])))

# Converting a list to set
log_variable("set([1, 2, 3, 3, 4])", set([1, 2, 3, 3, 4]))
log_variable("type(set([1, 2, 3, 3, 4]))", type(set([1, 2, 3, 3, 4])))

# Converting int to binary
log_variable("bin(10)", bin(10))
log_variable("bin(33)", bin(33))

# Converting int to hexadecimal
log_variable("hex(10)", hex(10))

# Converting binary to decimal
log_variable("int(bin(10))", int(bin(10), 2))

# Converting hex to decimal
log_variable("int(hex(33), 16)", int(hex(33), 16))