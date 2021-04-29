from itertools import *
from log_variable import log_variable

"""
itertools provides functions to use with iterable objects
"""
list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

# chain takes various sequences and chain them together
chained_iterator = chain(list1, list2)
log_variable("type(chained_iterator)", type(chained_iterator))
for i in chained_iterator:
    log_variable("i", i)
chained_list = list(chain(list1, list2))
log_variable("chained_list", chained_list)

# count function returns an iterator that generates consecutive integers until it stops
# arguments: count(starting_point, step)
for i in count(10, 2.5):
    if i <= 50:
        log_variable("i", i)
    else:
        break

# cycle function returns an iterator that simply repeat the value given as argument
a = range(11, 16)
counter = 0
for i in cycle(a):
    print(i)
    counter = counter + 1
    if counter > 10:
        break

# filterfalse function is similar to filter function but it returns the elements that return false to filter function
filterfalse_iterator = filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])
for element in filterfalse_iterator:
    log_variable("element", element)

# islice function - an alternative of old way of slicing
range_list = list(range(10))
log_variable("range_list[2:9:2]", range_list[2:9:2])

iter_islice = islice(range(10), 2, 9, 2)
log_variable("type(iter_islice)", type(iter_islice))
log_variable("list(iter_islice)", list(iter_islice))
