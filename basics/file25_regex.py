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
search method - searches for any occurrence in the entire string 
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
log_variable("regex_result.groups()", regex_result.groups()) # Returns a tuple with all the matched groups
