"""
reference: https://www.tutorialspoint.com/python3/python_reg_expressions.htm
\d - digits
\s - new line, tab and space characters
\w - word character, letters (upper-case or lower-case), numbers and underscore
\D - non digit characters
\S - non space characters
\W - non word characters
\A - matches characters in the beginning of the string
\Z - matches characters in the end of the string
"""

import re
from log_variable import log_variable

my_string = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."

# match() method - searches the pattern in a string but only at the beginning of the string.
log_variable(r're.match("You", my_string)', re.match("You", my_string))
log_variable(r're.match("abc", my_string)', re.match("abc", my_string))

# the match method does not find result if the occurrence is not in the beginning of the file
log_variable(r're.match("learn", my_string)', re.match("learn", my_string))

match_you = re.match("You", my_string)
log_variable("match_you.group()", match_you.group())

# ignoring case to match
log_variable(r're.match("you", my_string, re.I)', re.match("you", my_string, re.I))

"""
search method - searches for the first occurrence of the expression in the entire string 
"""
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222        L"
"""
group 1: ->(.+?) +<-
    .+ = matches any character except for new line character one or more times
    ?  = turn off greedy (finds the most characters as possible) mode, stops the match when it finds the space character after the group. If removed, the group result matches also the spaces characters after the group
     + = one or more spaces are expected in the string
group 2: ->(\d) +<-
    \d = any decimal digit from 0 to 9
     + = one or more spaces are expected in the string
group 3: ->(.+?)\s{2,}(\w)*<-
     .+     = matches any character except for new line character one or more times
     \s{2,} = \s (matches a sequence of white space character - space, tab), {2,} match a sequence of at least 2 characters preceeding the curly braces,
 group 4: ->(\w)*<- 
     \w = matches word characters - [a-z], [A-Z] [0-9]  and _
     *  = matches zero or more occurrences of the character defined before it 
"""
regex_result = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
log_variable("regex_result.group(1)", regex_result.group(1))
log_variable("regex_result.group(2)", regex_result.group(2))
log_variable("regex_result.group(3)", regex_result.group(3))
log_variable("regex_result.group(4)", regex_result.group(4))
log_variable("regex_result.groups()", regex_result.groups())  # Returns a tuple with all the matched groups

"""
findall method
"""
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222        L"
"""
    \d\d       = two consecutive digits
    \.         = matches the dot character
    \d{2}      = two consecutive digits
    [0-9][0-9] = range of characters to match two consecutive digits
    [0-9]{1,3} = range of characters that can appear 1, 2 or three times
"""
findall_result = re.findall(r"\d\d.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
log_variable("findall_result", findall_result)

# applying groups to the above regex
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222   10.10.10.10    L"
findall_regex_result = re.findall(r"(\d\d).(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
log_variable("findall_regex_result", findall_regex_result)

"""
sub method - replaces all occurrences of the specified pattern
"""
arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222        L"
sub_result = re.sub(r"\d", "7", arp)
log_variable("sub_result", sub_result)

"""
Other examples using regex expressions
"""
# finding first non digits characters in a string
new_string_1 = "I enjoy learning programming languages such as Python 3"
non_digits_search = re.search(r"\D+", new_string_1)
log_variable("non_digits_search", non_digits_search)
log_variable("non_digits_search.group()", non_digits_search.group())
log_variable("non_digits_search.group(0)", non_digits_search.group(0))

# finding first non space characters
non_space_search = re.search(r"\S+", new_string_1)
log_variable("non_space_search", non_space_search)
log_variable("non_space_search.group()", non_space_search.group())

# finding first non word characters
non_word_search = re.search(r"\W", new_string_1)
log_variable("non_word_search", non_word_search)
log_variable("new_string_1.index(non_word_search.group())", new_string_1.index(non_word_search.group()))

# matching the string starts with character
char_beginning_search = re.search(r"\AI", new_string_1)
log_variable("char_beginning_search.group()", char_beginning_search.group())

char_beginning_search = re.search(r"\AF", new_string_1)  # returns NoneType as the string not starts with F
log_variable("type(char_beginning_search)", type(char_beginning_search))

# matching the string ends with character
end_char_search = re.search(r"3\Z", new_string_1)
log_variable("end_char_search", end_char_search)
log_variable("end_char_search.group()", end_char_search.group())

"""
set of character in regex expressions
"""
# matching all lower case characters
lower_case_search = re.findall(r"[a-z]", new_string_1)
log_variable("lower_case_search", lower_case_search)

# matching all upper case characters
upper_case_search = re.findall(r"[A-Z]", new_string_1)
log_variable("upper_case_search", upper_case_search)

# matching lower case using a specific set of characters - a, b, c or d
lower_case_specific_set_result = re.findall(r"[a-d]", new_string_1)
log_variable("lower_case_specific_result", lower_case_specific_set_result)

# matching specific characters
lower_specific_chars_result = re.findall(r"[abn]", new_string_1)
log_variable("lower_specific_chars_result", lower_specific_chars_result)

# matching all characters excepting a
set_except_result = re.findall(r"[^a]", new_string_1)
log_variable("set_except_result", set_except_result)

# matching any digit from zero to nine
set_digit_result = re.findall(r"[0-9]", new_string_1)
log_variable("set_digit_result", set_digit_result)

# matching digits between 1 to 5
set_specific_set_result = re.findall(r"[1-5]", new_string_1)
log_variable("set_specific_set_result", set_specific_set_result)

# matching specific digits 1, 3 or 5 in the string
specific_digits_result = re.findall("r[135]", new_string_1)
log_variable("specific_digits_result", specific_digits_result)
