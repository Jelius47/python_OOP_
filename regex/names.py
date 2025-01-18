import re

my_strings='''
Hello Worrld
123
Mr Simpson
Kramajong
Maskrat 
Mrs Simspon
Mr. Brown
Ms Smith
Mr. T
brew
breeze

user emails
jeliusheneriko47@gmail.com
jelius.heneriko@eastc.ac.com
Jesusmyfriend@heaven.com
'''

patern = re.compile(r'Mr\.?\s\w+')
# \s for the space and \w for a word but + as a quantifier for one or more word
# \.? means that the dot may be optional /not necessarly to be found


# Again we can use the conditions 
pattern_conditions = re.compile(r"(Mr|Ms|Mrs)\.?\s?\w+")
matches_p= pattern_conditions.finditer(my_strings)

for match in matches_p:
    print(match)

# how do i capture emails with  special characters

# Creating a patern to capture the emails   
patern_email = re.compile(r"[a-zA-Z0-9.?]+@[a-zA-z-]+.[a-z]+(.[a-z]+)?")
match_e = patern_email.finditer(my_strings)

for match in match_e:
    print(match.group())# using group() will help us to get only the characters 
    print(match.group(1))# remember ( ) i have used this to group for the eastc
    # emails at first so we have one grop after all
    