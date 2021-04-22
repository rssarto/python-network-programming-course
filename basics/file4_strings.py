# Invalid identifiers for variable name
# var-1="Teste"
# 1_var="Test"

def log_variable(var_name, var_value):
    print(str.format("{} ->{}<-", var_name, var_value))


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
def print_template(model, wan_slots, os_version):
    var_template = "Cisco model: %s, %d WAN slots, IOS %.1f"
    log_variable(str.format("{} % ({}, {}, {})", var_template, model, wan_slots, os_version),
                 var_template % (model, wan_slots, os_version))


print_template("2600XM", 2, 12.4)
print_template("2691XM", 4, 12.3)
print_template("7200XR", 8, 15.4)

# -> formatting using f-strings
model = "2600XM"
slots = 4
ios = 12.3
log_variable("f\"Cisco model: {model}, {slots} WAN slots, IOS {ios}\"",
             f"Cisco model: {model}, {slots} WAN slots, IOS {ios}")
log_variable("f\"Cisco model: {model}, {slots} WAN slots, IOS {ios * 2}\"",
             f"Cisco model: {model}, {slots} WAN slots, IOS {ios * 2}")
log_variable("f\"Cisco model: {model.lower}, {slots} WAN slots, IOS {ios}\"",
             f"Cisco model: {model.lower()}, {slots} WAN slots, IOS {ios}")

# -> string slice - syntax my_string[10: 15], it will no include 15
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
log_variable("string1[5: 14]", string1[5: 14])  # print from fifth to thirteenth character
log_variable("string1[5: 15]", string1[5: 15])  # print from fifth to fourteenth character
log_variable("string1[5:]", string1[5:])  # print from fifth character till the end
log_variable("string1[:10]", string1[:10])  # print the first nine characters
log_variable("string1[-1]", string1[-1])  # in reverse index, print the last character from string
log_variable("string1[-2]", string1[-2])  # in reverse index, print the second character from right to left
log_variable("string1[-9: -1]", string1[-9: -1])  # in reverse index, print from ninth character to the last character
log_variable("string1[-5: ]", string1[-5:])  # print the last 5 characters
log_variable("string1[:-5]", string1[:-5])  # print from the beginning and skip the last 5 characters
log_variable("string1[::2]", string1[::2])  # print every 2 characters from string
log_variable("string1[::-1]", string1[::-1])  # print string in reverse order

# -> more on slice strings with steps
string_numbers = "0123456789"
log_variable("string_numbers[::2]", string_numbers[::2])  # print only even numbers
log_variable("string_numbers[1::2]", string_numbers[1::2])  # print only odd numbers
log_variable("string_numbers[1:7:2]", string_numbers[1:7:2])  # print odd numbers less than 7
log_variable("string_numbers[1:string_numbers.index(\"7\"):2]",
             string_numbers[1:string_numbers.index("7"):2])  # print odd numbers less than 7

print(
    """
    String notebooks from course
    """)
# Defining a string on multiple lines, using triple quotes and the line continuation character ( \ )
my_string = '''this\
is\
my\
first\
string'''

# Strings - indexing
a = "Cisco Switch"
a.index("i")
log_variable("a.index(\"i\")", a.index("i"))

# Strings - character count
a = "Cisco Switch"
a.count("i")
log_variable("a.count(\"i\")", a.count("i"))

# Strings - finding a character
a = "Cisco Switch"
a.find("sco")
log_variable("a.find(\"sco\")", a.find("sco"))

# Strings - converting the case
a = "Cisco Switch"
a.lower()  # lowercase
log_variable("a.lower()", a.lower())

a.upper()  # uppercase
log_variable("a.upper()", a.upper())

# Strings - checking whether the string starts with a character
a = "Cisco Switch"
a.startswith("C")
log_variable("a.startswith(\"C\")", a.startswith("C"))

# Strings - checking whether the string ends with a character
a = "Cisco Switch"
a.endswith("h")
log_variable("a.endswith(\"h\")", a.endswith("h"))

# Strings - removing a character from the beginning and the end of a string
a = "   Cisco Switch   "
a.strip()  # remove whitespaces
log_variable("a.strip()", a.strip())

b = "$$$Cisco Switch$$$"
b.strip("$")  # remove a certain character
log_variable("b.strip(\"$\")", b.strip("$"))

# Strings - removing all occurences of a character from a string
a = "   Cisco Switch   "
a.replace(" ", "")  # replace each space character with the absence of any character
log_variable("a.replace(\" \", \"\")", a.replace(" ", ""))

# Strings - splitting a string by specifying a delimiter; the result is a list
a = "Cisco,Juniper,HP,Avaya,Nortel"  # the delimiter is a comma
a.split(",")
log_variable("a.split(\",\")", a.split(","))

# Strings - inserting a character in between every two characters of the string / joining the characters by using a delimiter
a = "Cisco Switch"
"_".join(a)
log_variable("\"_\".join(a)", "_".join(a))

# Additional methods (source: https://www.tutorialspoint.com/python3/python_strings.htm)

# Capitalizes first letter of string.
a = "cisco switch"
a.capitalize()
log_variable("a.capitalize()", a.capitalize())

# Removes all leading whitespace in string.
a = "     cisco switch      "
log_variable("a.lstrip()", a.lstrip())

# Removes all trailing whitespace of string.
a = "     cisco switch      "
log_variable("a.rstrip()", a.rstrip())

# Inverts case for all letters in string.
a = "cisco Switch"
my_string.swapcase()
log_variable("a.swapcase()", a.swapcase())

# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
a = "cisco Switch"
log_variable("a.title()", a.title())

# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
log_variable("\"1234\".isalnum()", "1234".isalnum())
log_variable("\"#$%\".isalnum()", "#$%".isalnum())
log_variable("\"#$%a\".isalnum()", "#$%a".isalnum())
log_variable("\"+\".isalnum()", "+".isalnum())

# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
my_string.isalpha()
log_variable("\"1\".isalpha()", "1".isalpha())
log_variable("\"abcdefghijklmnopqrst\".isalpha()", "abcdefghijklmnopqrst".isalpha())
log_variable("\"12345abcdefghijklmnopqrst\".isalpha()", "12345abcdefghijklmnopqrst".isalpha())

my_string.isdigit()
# Returns true if string contains only digits and false otherwise.
log_variable("\"1000.00\".isdigit()", "1000.00".isdigit())
log_variable("\"1200\".isdigit()", "1200".isdigit())

my_string.islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
log_variable("\"howe town\".islower()", "howe town".islower())
log_variable("\"Home town\".islower()", "Home town".islower())

my_string.isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.

my_string.isspace()
# Returns true if string contains only whitespace characters and false otherwise.

my_string.istitle()
# Returns true if string is properly "titlecased" and false otherwise.

my_string.isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

# Strings - concatenating two or more strings
a = "Cisco"
b = "2691"

a + b

# Strings - repetition / multiplying a string
a = "Cisco"

a * 3

# Strings - checking if a character is or is not part of a string
a = "Cisco"

"o" in a

"b" not in a

# Strings - formatting v1
"Cisco model: %s, %d WAN slots, IOS %f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.1f" % ("2600XM", 2, 12.4)
"Cisco model: %s, %d WAN slots, IOS %.2f" % ("2600XM", 2, 12.4)

# Strings - formatting v2
"Cisco model: {}, {} WAN slots, IOS {}".format("2600XM", 2, 12.4)
"Cisco model: {0}, {1} WAN slots, IOS {2}".format("2600XM", 2, 12.4)

# Strings - formatting v3 (f-strings)
a = "2600XM"
b = 2
c = 12.4
f"Cisco model: {a}, {b} WAN slots, IOS {c}"

# Strings - slicing
string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"

string1[
5:15]  # slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
string1[5:]  # slice starting at index 5 up to the end of the string
string1[:10]  # slice starting at the beginning of the string up to, but NOT including, index 10
string1[:]  # returns the entire string
string1[-1]  # returns the last character in the string
string1[-2]  # returns the second to last character in the string
string1[-9:-1]  # extracts a certain substring using negative indexes
string1[-5:]  # returns the last 5 characters in the string
string1[:-5]  # returns the string minus its last 5 characters
string1[::2]  # adds a third element called step; skips every second character of the string
string1[::-1]  # returns string1's elements in reverse order

# sets - mutable
# frozensets - immutable
# tuples - immutable
# ranges
# dictionaries - mutables
# None

# Raw literals - a way to tell python's interpreter to read all characters as literals and not as special codes
var_raw_string = r"\ntest\tblabla"
log_variable("var_raw_string", var_raw_string)
