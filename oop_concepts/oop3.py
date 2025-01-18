# Inheritance in python What  coud be done is overriding , extending and at last inheriting the base class
class Employee:# this act as the bse class
    def __init__(self,name,age,salary):
        self.name = name
        self.age =age    
        self.salary = salary
    def work(self):
        print(f"{self.name} is working...")

# Child classes inheriting from the base class


class SoftwareEngineer(Employee):
    def __init__(self, name, age,salary,level):
        # Overriding the base class __init__ method
        super().__init__(name, age,salary)# the super function is used to inherit the base class __init__ properties
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging")
        # Child classes inheriting from the base clas
    def work(self):
        print(f"{self.name} is coding...")
        

class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing")
    
    def work(self):# Overriding the base class work method
        print(f"{self.name} is designing")


# Object instantiation 
se = SoftwareEngineer("Max",25,5000,"Junior")
d = Designer("Philipp",27,7000)

# Printing the output 
print(se.age,se.name)
print(d.age,d.name)
print(se.level)


# Polymorphism - means many shapes,for the codes to run on the super class and also for sny subclass
employees = [SoftwareEngineer("Max",25,5000,"Junior"),
            SoftwareEngineer("Lisa",30,7000,"Senior"),
            Designer("Philipp",27,7000)]


# Assuminng we are in HR dept and we want to motivate employees without knowing their specific works
# taking the employee list and looping through it and calling the work method irrespectively of the role 

def motivate_employee(employees):
    for employee in employees:
        employee.work()

motivate_employee(employees)