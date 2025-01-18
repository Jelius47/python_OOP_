import re 

testi_string = "345678sabc234abc234ABC"

pattern = re.compile(r"abc")

matches = pattern.finditer(testi_string)
matches2 = pattern.finditer(testi_string)

# alternatively
# matches = re.finditer(r"abc",testi_string)
# The r -- signifies that the raw strings are considered including 
# special characters \t or \n that they will be considered as other characters


# methods to find regular expressions



# 1.findall()
matches_all = pattern.findall(testi_string)

for match in matches_all:
    print(match)

    # abc
    # abc this will print only the required findings
# The  **key finditer() -- this will print the objects and detailed information
for match in matches:
    print(match)
# The output features two objects that can be found from the string 
# <re.Match object; span=(7, 10), match='abc'>
# <re.Match object; span=(13, 16), match='abc'>


# 2. match() determines if the expressions matches the expression even at the beginning of the string 
match = pattern.match(testi_string)

# This will return None -- because it only return the matching value at the starting on the given string
print(match)

# 3. search() -- This method will only return the first  string related to the targeted string in our 
# as an object.

match2 = pattern.search(testi_string)
print(match2)


# Other functions that could be used to manipulate the regular string 

# span(),start(),end()

for match in matches2:
    print(match.span(),match.start(),match.end())

# The group() -- This will print the group of string it got from the main string 

matches3 = pattern.finditer(testi_string)

for match in matches3:
    print(match.group())


# Dealing with the Meta characters .  $ + ? ^ * () {} [] \ |

# . --Any character except a newline character
# ^ -- Starts with "^hello"
# $ -- Ends with "world$"
# * -- Zero or more occurances "aix*"
# + -- One or more occurfances "aix+"
# {} -- Exactly the specified number of occurances "al{2}"
# [] -- A set of characters "[a-m]"
# \ -- Special sequence (or escape special characters) "\d"
# | -- Either or "Falls|Stays"
# () -- Capture and group

# More special characters
# \d : Matches any decimal digit; [0-9]
# \D : Matches any non-digit character ;
# \s : Matches any whitespace character ;(space " " tab "\t" newline "\n")
# \S : Matches any non-whitespace character;
# \w : Matches any alphanumeric (word) character; [a-z A-Z 0-9]
# \W : Matches any non-alphanumeric character
# \b : Matches where the specified characters are at the begining or at the end of the word r"\bbain" or r"bain\b"
# \B : Matches where the specified characters are present,but not at the beginning (or at the end of the word)

# Sample implementations
test_string = 'hello 123_ heyho hohey'

# pattern2 =re.compile(r"\d") # Look for any Digit 
pattern2 =re.compile(r"\bhello") # Look for any word at the starting of a word block
match_str = pattern2.finditer(test_string)

# for match in match_str:
    # print(match)

# pattern3 = re.compile(r'[0-9]') # Also r[23-] means it will look for the digits 2 and 3 and the dash(-) only
# pattern3 = re.compile(r'[hello]') # Also you could put this in this way 
# pattern3 = re.compile(r'[a-zA-Z0-9]') # This will also include upper case letters and numbers also
pattern3 = re.compile(r'[a-z]') # Looking for patterns when focusing on the letters set
match_str3 = pattern3.finditer(test_string)
# for match in match_str3:
    # print(match)


# Working with QUANTIFIERS 
# * : 0 or more
# + : 1 or more
# ? : 0 or 1 ; -- That we are looking for a character that might be there or not 
# {4} : Exact character
# {4,6} : Range numbers (min,max)
# Fuctions that can be used to modify the object split() , sub()


# Worked example 
test_string4 = "hello_123"

pattern4 = re.compile(r"\d*")# First '\d'-looks for any digits then * --checks for any digits either 0 or more 

match4 = pattern4.finditer(test_string4)
for match in match4:
    print(match)


pattern4_ = re.compile(r"_\d")# here we are looking for digit that have undersscore 
# pattern4_ = re.compile(r"_?\d") # This will make the searching of underscores optional
# pattern4_ = re.compile(r"_\d{10}") # This will only focus on 10 digits only ie: you are looking for a phone number
match4_ = pattern4.finditer(test_string4)

for mathchX in match4_:
    print(mathchX)

# Note :
# DO NOT USE '/' IT WONT WORK INSTEAD USE THIS '\'

