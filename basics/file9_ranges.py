"""
Range data type
Is not possible to slice a range
"""
from log_variable import log_variable

log_variable("range(10)", range(10))
log_variable("type(range(10)", type(range(10)))
log_variable("list(range(10))", list(range(10)))
log_variable("range(10)[0]", range(10)[0])
log_variable("range(10)[-1]", range(10)[-1])
log_variable("10 in range(10)", 10 in range(10))
log_variable("10 not in range(10)", 10 not in range(10))
log_variable("list(range(10))[2:5]", list(range(10))[2:5])

# for index in range(10):
#     log_variable("index", index)
