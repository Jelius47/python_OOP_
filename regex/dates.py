import re

dates = '''
01.04.2021
2020.04.23

2020-02-12
2020-02-13
2020/04/12

2020_01_23
2020_04_07

'''

# pattern = re.compile(r"\d\d\d\d.\d\d.\d\d")
# pattern = re.compile(r"\d\d\d\d-\d\d-\d\d") # For specific dates that have dash amaong them 
# what if we want to look for more than one pattern within dates /,_,- then we will use sets
pattern = re.compile(r"\d\d\d\d[/-]\d\d[/-]\d\d")


matches = pattern.finditer(dates)
# \d\d\d\d for the first four digits of year
# . for any character except newline 
# for match in matches:
#     print(match)



# Now lets say I am looking for dates in february or June only

pattern_month = re.compile(r"\d\d\d\d.0[21].\d\d")
matches_month = pattern_month.finditer(dates)

# for match in matches_month:
#     print(match)
# # Now lets use the quantifier

pattern_quantifier = re.compile(r"\d{4}.0[21].\d{2}")
matches_month2 = pattern_quantifier.finditer(dates)

for match in matches_month2:
    print(match)
