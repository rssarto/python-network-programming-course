"""
Functions to support you on how to find out a module works
"""
import sys
from log_variable import log_variable

# describe the module features
help(sys)

print("---> dir function <---")

# shows the functions available in sys module
print(dir(sys))
