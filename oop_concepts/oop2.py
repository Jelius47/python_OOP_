# Functions in oop
from oop1 import sof_1,sof_2

# def code(se):
#     print(f"{se[1]} is writting code...")
# Here anybody can acess the function even if does'nt code 

class SoftwareEngineer:
    # Also we can formulate class attribute 
    alias = "Keyboard Magician"

    def __init__(self,name,age,level,salary):# Afunction that is called when we create an object
        # Instance attributes only belongs to one object that is being created
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        
# Instance metod
    def code(self):
        print(f"{self.name} is writting code...")

    def code_in_lang(self,language):
        print(f"{self.name} is cooding in {language}")

    # def information(self):
    #     information  = f"Your informations are name = {self.name},age = {self.age},level = {self.level}"
    #     return information

# dunder methods - Function that are not part of the class but are used to manipulate the class,
# they are predefined functions
    def __str__(self):
        information = f"Your informations are name = {self.name},age = {self.age},level = {self.level}"
        return information
    def __eq__(self, value):
        return self.name == value.name and self.age ==  value.age

# Want to create a function that will not use the self parameter
# We use the @staticmethod decorator to create a static method and we can call it without creating an object
    @staticmethod
    def entry_Salary(age):
        if age > 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

# instanciate an object

software_e1_ = SoftwareEngineer("Max",20,"Junior",5000)
software_e2_ = SoftwareEngineer("Lisa",20,"Senior",7000)
software_e3_ = SoftwareEngineer("Lisa",20,"Senior",7000)

# Print outputs
print(software_e2_== software_e3_) # this will return true because the object are the same
print(software_e1_ == software_e2_) # this will return false because the object are different interms of memeory
# address hence the use of __eq__()

software_e1_.code() # Excecute the code method
software_e1_.code_in_lang("C++")
print(software_e1_)

# Accessing the function entry salary without an object
print(SoftwareEngineer.entry_Salary(20)) # apart from there it will shout an error else we shall put the decorator
print(software_e1_.entry_Salary(40))
# A little bit of magic WHEN imported script oop1.py  i also the script was excecuted 
# showing the result of the printed values in the oop1.py 