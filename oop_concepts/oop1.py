# Position,name,age,experience,salary

sof_1 = ["software Engineer","Max",20,"Junior",5000]
sof_2 = ["software Engineer","Lisa",20,"Senior",7000]

# The problem becomes that we are error prone 

# Lets create a class

class SoftwareEngineer:
    # Also we can formulate class attribute 
    alias = "Keyboard Magician"

    def __init__(self,name,age,level,salary):# Afunction that is called when we create an object
        # Instance attributes only belongs to one object that is being created
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        

# instanciate an object

software_e1_ = SoftwareEngineer("Max",20,"Junior",5000)
software_e2_ = SoftwareEngineer("Lisa",20,"Senior",7000)
# print(software_e1_.name,software_e1_.age)



# We can not access the insgtance attributes directly
# print(software_e1_.name) will throw an error  

# print(SoftwareEngineer.alias,SoftwareEngineer.level) Will shout an error


# Recap 
#  class is a blue print 
#  object is an instance of a class
#  Instance are unique for each object
#  Attribute are of two types class and and functional attributes
