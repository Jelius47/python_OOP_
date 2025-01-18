# Generator function - A function with a yield keyword rather than a return keyword
# they are useful in memory managemnt 
def mygenerator():
    yield 3
    yield 2
    yield 1

# Creating the object for my generate
g = mygenerator()
# this will print the object g
print(g)

# how to access the values returned in mygenerator()
# 1. Through for loops

# for i in g:
#     print(i)

# Through the next() function this will provide the single value of yield and only when called for instance 

# value = next(g)
# print(value) # this will only print 1 
# value =next(g)
# print(value) # Will print 2 since is the next value form our object until the code terminates

# Generators could be used as input to other functions that takes iterables

# Also 
# a = sum(g) # Returns a sum of values from the function
b = sorted(g) # will return a sorted list of values 
# print(a)
print(b)

# Second generator
def my_second_genrattor(num):
    print("Starting ...")

    while num > 0:
        yield num
        num -= 1

# Creating my object
cd = my_second_genrattor(4)

# How to run it 
# using next()
value = next(cd) # If i'll only run this it run my whole generator and only print my first statment without yielding

print(value) #When i prints the first value of num will be returned 
#  when i rewrite the print statment again it will remember where i ended at 
print(next(cd))