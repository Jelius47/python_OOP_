import re

# split() , sub()

# here is our test string
test_string = '123abc3449bifvodiaoik iodfopfd789ncknxjcohbzbfjhabmcbzjbcbfai'

patern = re.compile(r"f")
split = patern.split(test_string)
 
# for match in split:
#     print(match)
print(split) # This will give the list of our splitted terms 


# Using the sub()
pattern = re.compile(r"[a-z]\S")
substituter = pattern.sub("Jesus wisdom over me\n",test_string)

print(substituter)