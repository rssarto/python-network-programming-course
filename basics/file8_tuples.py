"""
Immutable list
Store data in form of a sequence, ordered of not unique elements. Duplicates elements are allowed
"""

from log_variable import log_variable

my_tuple = ()
log_variable("type(())", type(()))

# creating a tuple with one element
# -> right method
one_element_tuple = (9,)
log_variable("type((9,))", type((9,)))

# -> wrong method
log_variable("(9)", type((9)))

# interacting with tuple's elements
log_variable("(1, 2, 3, 4, 5)[0]", (1, 2, 3, 4, 5)[0])
log_variable("(1, 2, 3, 4, 5)[1]", (1, 2, 3, 4, 5)[1])
log_variable("(1, 2, 3, 4, 5)[-1]", (1, 2, 3, 4, 5)[-1])
log_variable("(1, 2, 3, 4, 5)[-2]", (1, 2, 3, 4, 5)[-2])

my_tuple_1 = (1, 2, 3, 4, 5)
try:
    my_tuple_1[1] = 10
except TypeError as change_err:
    log_variable("err", change_err)
    log_variable("err.args", change_err.args)

try:
    del my_tuple_1[1]
except TypeError as delete_err:
    log_variable("err", delete_err)
    log_variable("err.args", delete_err.args)

# assigning tuple values to variables
# tuple packing and unpacking
my_tuple_2 = ("Cisco", "2600", "12.4")
(vendor, model, ios) = my_tuple_2
log_variable("(vendor, model, ios) = my_tuple_2", f"vendor = {vendor}, model = {model}, ios = {ios}")

my_tuple_3 = (1, 2, 3, 4)
try:
    (x, y, z) = my_tuple_3
except ValueError as unpacking_err:
    log_variable("unpacking_err", unpacking_err)
    log_variable("unpacking_err.args", unpacking_err.args)

try:
    (a, b, c, d, e) = my_tuple_3
except ValueError as unpacking_err:
    log_variable("unpacking_err", unpacking_err)
    log_variable("unpacking_err.args", unpacking_err.args)

# Tuples vs List
# Tuples() (fixed length) are immutable whilst lists[] (variable length) are mutable
log_variable("dir(())", dir(()))
log_variable("dir([])", dir([]))

# Tuples methods
log_variable("len((1, 2, 3, 4))", len((1, 2, 3, 4)))
log_variable("min((1, 2, 3, 4))", min((1, 2, 3, 4)))
log_variable("max((1, 2, 3, 4))", max((1, 2, 3, 4)))
log_variable("(3, 4, 5) + (1, 2, 3, 4)", (3, 4, 5) + (1, 2, 3, 4))
log_variable("(1, 2, 3, 4) * 2", (1, 2, 3, 4) * 2)
log_variable("(1, 2, 3, 4)[0: 2]", (1, 2, 3, 4)[0: 2])
log_variable("(1, 2, 3, 4)[:2]", (1, 2, 3, 4)[:2])
log_variable("(1, 2, 3, 4)[1:]", (1, 2, 3, 4)[1:])
log_variable("(1, 2, 3, 4)[:]", (1, 2, 3, 4)[:])
log_variable("(1, 2, 3, 4)[-1]", (1, 2, 3, 4)[-1])
log_variable("(1, 2, 3, 4)[-4: -1]", (1, 2, 3, 4)[-4: -1])
log_variable("(1, 2, 3, 4)[-4: -2]", (1, 2, 3, 4)[-4: -2])
log_variable("(1, 2, 3, 4)[: -1]", (1, 2, 3, 4)[: -1])
log_variable("(1, 2, 3, 4)[::-1]", (1, 2, 3, 4)[::-1])
log_variable("(1, 2, 3, 4)[::2]", (1, 2, 3, 4)[::2])
log_variable("2 in (1, 2, 3, 4)", 2 in (1, 2, 3, 4))
log_variable("9 in (1, 2, 3, 4)", 9 in (1, 2, 3, 4))
log_variable("9 not in (1, 2, 3, 4)", 9 not in (1, 2, 3, 4))

# Removing Tuple from memory
del my_tuple_3
try:
    log_variable("del my_tuple_3", my_tuple_3)
except NameError as name_err:
    log_variable("my_tuple_3", name_err)
