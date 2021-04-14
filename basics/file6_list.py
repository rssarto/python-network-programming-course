from file4_strings import log_variable

list1 = []
log_variable("type(list1)", type(list1))

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
log_variable("list1", list1)
log_variable("len(list1)", len(list1))
log_variable("list1[0]", list1[0])  # First element
log_variable("list1[1]", list1[1])  # Second element
log_variable("list1[-1]", list1[-1])  # Last element
log_variable("list1[-2]", list1[-2])  # The second element from right to left
try:
    log_variable("list1[100]", list1[100])
except IndexError as err:
    log_variable("index error", err)
    log_variable("index error type", type(err))
    log_variable("index error args", err.args)

#  Replace a value in the list
list1[2] = "HP"
log_variable("list1[2]", list1[2])

"""
List methods
"""
list2 = [-11, 2, 12]

# minimum value in the list
log_variable("min(list2)", min(list2))

# maximum value in the list
log_variable("max(list2)", max(list2))

list3 = ["a", "b", "c"]
log_variable("min(list3)", min(list3))
log_variable("max(list3)", max(list3))

# Comparison operators are not supported with different data types
# In that case, if you have a alphanumeric list it will throw an error
try:
    log_variable("max(list1)", max(list1))
except TypeError as err:
    log_variable("index error", err)
    log_variable("index error type", type(err))
    log_variable("index error args", err.args)

# append an element to the list
list1.append(100)
log_variable("list1.append(100)", list1)

# removing an element from the list
del list1[4]
log_variable("del list1[4]", list1)

list1.pop(0)
log_variable("list1.pop(0)", list1)

list1.remove("Juniper")
log_variable("list1.remove(\"Juniper\")", list1)

# inserting an element at a particular position
list1.insert(2, "Nortel")
log_variable("list1.insert(2, \"Nortel\")", list1)

# inserting a list into another list
list1.extend([9, 99, 999])
log_variable("list1.extend([9, 99, 999])", list1)
log_variable("list1 + [5, 5, 555]", list1 + [5, 5, 555])


# fetching the element's index from the list
log_variable("list1.index(-11)", list1.index(-11))

# counting the ocurrences of an element in the list
log_variable("list1.count(10)", list1.count(10))

# sorting a list
numbers_list = [9, 99, 999]
numbers_list.append(1)
numbers_list.append(25)
numbers_list.append(500)
numbers_list.sort()
log_variable("numbers_list.sort()", numbers_list)
numbers_list.reverse()
log_variable("numbers_list.reverse()", numbers_list)
sorted(numbers_list)
log_variable("sorted(numbers_list)", numbers_list)
sorted(numbers_list, reverse=True)
log_variable("sorted(numbers_list, reverse=True)", numbers_list)

# slicing
log_variable(" [1, 2, 3, \"a\", \"b\", \"c\"][0: 4]", [1, 2, 3, "a", "b", "c"][0: 3])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][: 3]", [1, 2, 3, "a", "b", "c"][: 3])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][2: 5]", [1, 2, 3, "a", "b", "c"][2: 5])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][2:]", [1, 2, 3, "a", "b", "c"][2:])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][-1]", [1, 2, 3, "a", "b", "c"][-1])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][-2]", [1, 2, 3, "a", "b", "c"][-2])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][-4:-1]", [1, 2, 3, "a", "b", "c"][-4:-1])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][-3:]", [1, 2, 3, "a", "b", "c"][-3:])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][:-3]", [1, 2, 3, "a", "b", "c"][:-3])
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][::2]", [1, 2, 3, "a", "b", "c"][::2])  # Read list with step 2
log_variable("[1, 2, 3, \"a\", \"b\", \"c\"][::-1]", [1, 2, 3, "a", "b", "c"][::-1])  # List in reverse order



