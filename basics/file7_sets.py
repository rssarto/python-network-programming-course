"""
Set is unordered collection with unique elements
Are mutable
It does not throw any error when duplicating an element, it simply no add the element
"""
from log_variable import log_variable

log_variable("set([1, 2, 3, 4, 5, 2, 3])", set([1, 2, 3, 4, 5, 2, 3]))
log_variable("type(set([1, 2, 3, 4, 5, 2, 3]))", type(set([1, 2, 3, 4, 5, 2, 3])))
log_variable("{1, 2, 3, 4, 5, 2, 3}", {1, 2, 3, 4, 5, 2, 3})
log_variable("type({1, 2, 3, 4, 5, 2, 3})", type({1, 2, 3, 4, 5, 2, 3}))
log_variable("len({1, 2, 3, 4, 5, 2, 3})", len({1, 2, 3, 4, 5}))
log_variable("4 in {1, 2, 3, 4, 5}", 4 in {1, 2, 3, 4, 5})  # Check if list contains element
log_variable("11 in {1, 2, 3, 4, 5}", 11 in {1, 2, 3, 4, 5})
log_variable("11 not in {1, 2, 3, 4, 5}", 11 not in {1, 2, 3, 4, 5})

numbers_set = {1, 2, 5, 6, 4}
# Add element to set
numbers_set.add(3)
log_variable("numbers_set.add(3)", numbers_set)

# Remove element from set
numbers_set.remove(5)
log_variable("numbers_set.remove(5)", numbers_set)

# Set operations

# Intersection
log_variable("{1, 2, 3, 4}.intersection({3, 5, 8})", {1, 2, 3, 4}.intersection({3, 5, 8}))
log_variable("{1, 2, 3, 4}.intersection({3, 5, 8})", {3, 5, 8}.intersection({1, 2, 3, 4}))

# Difference
log_variable("{1, 2, 3, 4}.difference({3, 5, 8})", {1, 2, 3, 4}.difference({3, 5, 8}))
log_variable("{3, 5, 8}.difference({1, 2, 3, 4})", {3, 5, 8}.difference({1, 2, 3, 4}))

# Union
log_variable("{1, 2, 3, 4}.union({3, 5, 8})", {1, 2, 3, 4}.union({3, 5, 8}))

# Remove random element in the set
log_variable("{1, 2, 3, 4}.pop()", {1, 2, 3, 4}.pop())

# Cleaning all elements from set
numbers_set.clear()
log_variable("numbers_set.clear()", numbers_set)

"""
Frozen Sets - are immutable sets
Methods like add, remove, pop and clear do not exist in frozenset
"""
frozen_set1 = frozenset([1, 2, 3, 4])
log_variable("frozenset([1, 2, 3, 4])", frozenset([1, 2, 3, 4]))

frozen_set2 = frozenset([3, 4, 7])
log_variable("frozenset([3, 4, 7])", frozenset([3, 4, 7]))

log_variable("type(frozen_set1)", type(frozen_set1))

log_variable("frozen_set2.intersection(frozen_set2)", frozen_set1.intersection(frozen_set2))
log_variable("frozen_set2.intersection(frozen_set1)", frozen_set2.intersection(frozen_set1))
log_variable("frozen_set1.difference(frozen_set2)", frozen_set1.difference(frozen_set2))
log_variable("frozen_set2.difference(frozen_set1)", frozen_set2.difference(frozen_set1))
log_variable("frozen_set1.union(frozen_set2)", frozen_set1.union(frozen_set2))