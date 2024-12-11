# Encapsulation concepts - hiding of data methods
class SoftwareEngineer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._salary = None # note the single _underscore for private variables
        self.__bugs_solved  = 0 # note the double __underscore for private variables like really PRIVATE


    def code(self):
        self.__bugs_solved += 1
    # Acessing the private variable within the class
    def get_salary(self):
        return self._salary
    

    def set_salary(self,base_value):
        # check value, enforce constraints
        self._salary = self._calculate_salary(base_value)

    # creating a private method
    def _calculate_salary(self,base_value):
        if self.__bugs_solved < 10:
            return base_value
        elif self.__bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se =  SoftwareEngineer("Max",25)
# Incrementing the bugs solved by our most professional software engineer and a hard worker
for i in range(70):
    se.code()
# Now the base salary is 6000 times 2 He is a good worker
se.set_salary(6000)
print(se.get_salary())
