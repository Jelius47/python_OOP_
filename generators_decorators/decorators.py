# There are two types of decorators:
# 1. Function decorators
# 2. Class decorators
# Decorator- A function that takes another function as an argument 
# and extends the behaviour of the function without explictly modifying it
#  - It allows me to add new functionality to an existing function


# @mydecorator
# def doSomething():
#     pass
import functools

def  start_end_decorator(func):
    def wrapper():# Inner function wrapping our function
            # Before 
        print('Start')
        func()# Excecute the function
            # After
        print('End')
    return wrapper 
            

def print_name():
    print('Alex')

# print_name() excecuting the function itself 

# print_name = start_end_decorator(print_name)
# print_name()

# Now understanding that then we will use python decorators 
# Hence we can now extend the behaviour of our function print_name_with_decorator
@start_end_decorator
def print_name_with_decorator():
    print('Jesus')

# print_name_with_decorator() #Excecuting the function


# Now i need to receive arguments in my wrapper function

# This is going to be a template for my nice decorator 
def start_end_decorator_w_args(func):
    @functools.wraps(func) # This is to avoid confusion that to declare this is 
    # is the wrapper below and can be inherited to other funtions through the big function above
    def wrapper(*args,**kwargs):
        print('Starting')
        results = func(*args,**kwargs)
        print('The End')
        return results
    return wrapper

@start_end_decorator_w_args
def add5(x):
    return x + 5

# Excecuting the function
# add5(10)

# print(help(add5))# this will give more info about the function
# print(add5.__name__)#Before functools the function will fail to identify the function identity but after declaring 
#the wraps itwont confuse the python at all
 
# Defining the decorated funtion repeate
def repeate(num_times):
    def decorator_repeate(func):

        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeate


# Decorators with arguments ;)
@repeate(num_times = 3)
def greet(name):
    print(f"Hello {name}")

# greet("Jesus")


# Stacking decorators on top of each other 
def start_end_decorator_(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Lord Your Here")
        result = func(*args,**kwargs)
        print("I'll rejoice !!")
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = " ,".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")
        result = func(*args,**kwargs)

        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper



@debug
@start_end_decorator_
def say_hello(name):
    greet = f"Hello {name}"
    print(greet)
    return greet

# say_hello("Jesus")
# this will first run the @debug decorator and within it ,it will run this decorator 
# @start_end_decorator_ will be called and the function say_hello will be excecuted 
# within the the @debug operator and at last the last value from the @debug will be returned 


# Class decorators 


class Count_calls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs): # This is in order to write the class decorator this will make the calss to behave like a function
        self.num_calls+= 1
        print(f"This is excecuted {self.num_calls} times")
        return self.func(*args,**kwargs)

# Assuming we have the function

# My class decorator -Typically useful when in need to maintain and  or update a state
@Count_calls
def say_hello_to_me():
    print('Hello')

say_hello_to_me()
say_hello_to_me()

# Typical usecases of the decorators
# 1. Timer decorator to calculate the excecution time of the function
# 2. Debug decorator - to print out the information about the decorators
# 3.