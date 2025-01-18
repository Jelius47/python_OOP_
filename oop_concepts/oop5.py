# Decorators 
class SoftwareEngineer:
   def __init__(self):
      self._salary = None

   @property
   def salary(self):
        return self._salary
   @salary.setter
   def salary(self,value):
       self._salary = value

   @salary.deleter
   def salary(self):
       del self._salary 




# Accessing the property
se = SoftwareEngineer()
se.salary = 6000
print(se.salary)

# del se.salary
# print(se.salary)  # AttributeError: 'SoftwareEngineer' object has no attribute '_salary'