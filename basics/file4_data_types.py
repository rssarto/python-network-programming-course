# Invalid identifiers for variable name
# var-1="Teste"
# 1_var="Test"

def log_variable(var_name, var_value):
    print(str.format("{}: {}", var_name, var_value))


# strings - immutable
my_string_double_quotes = "this is my first string using double quotes\""
log_variable("my_string_double_quotes", my_string_double_quotes)

my_string_simple_quotes = 'this is my first string using simple quotes\''
log_variable("my_string_simple_quotes", my_string_simple_quotes)

my_string_triple_double_quotes = """ This 
is 
my 
first 
string 
using 
triple
double 
quotes.
"""
log_variable("my_string_triple_double_quotes", my_string_triple_double_quotes)

my_string_triple_single_quotes = '''This
is
my
first
string
using
triple
simple
quotes.
'''
log_variable("my_string_triple_single_quotes", my_string_triple_single_quotes)

escape_new_line_characters_string = '''This\
is\
my\
multiline\
string\
with\
no\
new\
line\
character
'''
log_variable("escape_new_line_characters_string", escape_new_line_characters_string)

# Accessing characters from a string using index
string_index_use = "Cisco Router"
# -> reading from left to right
log_variable("string_index_use[0]", string_index_use[0])
log_variable("string_index_use[2]", string_index_use[2])
log_variable("string_index_use[5]", string_index_use[5])

# -> reading from right to left
log_variable("string_index_use[-1]", string_index_use[-1])
log_variable("string_index_use[-4]", string_index_use[-4])

# -> string length
len(string_index_use)

# -> invalid index access, it'll throw an IndexError saying the index is out of range
try:
    log_variable("string_index_use[21]", string_index_use[21])
except IndexError as err:
    log_variable("index error", err)
    log_variable("index error type", type(err))
    log_variable("index error args", err.args)

another_string_var = "Cisco Switch"
# -> find the index of a string character
log_variable("another_string_var.index(\"w\")", another_string_var.index("w"))

# -> count how many times a characters happens in a string
log_variable("another_string_var.count(\"i\")", another_string_var.count("i"))

# -> finds a sequence of characters in a string returning the index position where the match starts or -1 when not found
log_variable("another_string_var.find(\"sco\")", another_string_var.find("sco"))
log_variable("another_string_var.find(\"Yzz\")", another_string_var.find("Y"))

# -> upper and lowercase - no changes is applied to the original string
another_string_var.lower()
another_string_var.upper()

# -> startswith and endswith - returns TRUE or FALSE
another_string_var.startswith("C")
another_string_var.endswith("h")

# -> string strip - eliminates all white spaces from beginning and end of string
strip_string = "    Cisco Switch     "
log_variable("strip_string.strip()", strip_string.strip())

another_strip_string = "$$$Cisco Switch$$$"
log_variable("another_strip_string.strip(\"$\")", another_strip_string.strip("$"))

# -> string replace
log_variable("strip_string.replace(\" \", \"\")", strip_string.replace(" ", ""))

# -> string split
delimited_string = "Cisco,Juniper,HP,Avaya,Nortel"
strip = delimited_string.split(",")
log_variable("delimited_string.strip(\",\")", str.format("{}:{}", strip, type(strip)))

# -> string join
log_variable("\"_\".join(another_string_var)", "_".join(another_string_var))

# -> string concatenation
var_cisco = "Cisco"
var_switch = "switch"
log_variable("var_cisco + \" \" + var_switch", var_cisco + " " + var_switch)

# -> string repetition
log_variable("var_cisco * 3", var_cisco * 3)

# -> check if a particular string is part of another string
log_variable("\"o\" in var_cisco", "o" in var_cisco)
log_variable("\"b\" in var_cisco", "b" in var_cisco)
log_variable("\"b\" in var_cisco", "b" not in var_cisco)

# -> String template - Cisco model: 2600XM, 2 WARN slots, IOS 12.4
log_variable("\"Cisco model: %s, %d WAN slots, IOS %f\" % (\"2600XM\", 2, 12.4)", "Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4))


# numbers - immutable
# booleans
# lists - mutable
# sets - mutable
# frozensets - immutable
# tuples - immutable
# ranges
# dictionaries - mutables
# None